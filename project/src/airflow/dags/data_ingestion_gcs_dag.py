import os
import logging

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
from datetime import datetime
from urllib.parse import urlparse





PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BUCKET_FOLDER = "github"
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET",'raw') 
path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
github_url = ["https://raw.githubusercontent.com/PetroIvaniuk/2022-Ukraine-Russia-War-Dataset/main/data/russia_losses_equipment.json", 
        "https://raw.githubusercontent.com/PetroIvaniuk/2022-Ukraine-Russia-War-Dataset/main/data/russia_losses_personnel.json"]




def get_filename(url):
    parsed_link = urlparse(url)
    filename = os.path.basename(parsed_link.path)
    return filename.replace('.json','')+'.csv'

def from_json_2_csv(url, path_to_local_home):
    import pandas as pd
    df = pd.read_json(url)
    filename = get_filename(url)
    df.to_csv(f"{path_to_local_home}/{filename}", index=False)


def format_to_parquet(url, path_to_local_home):
    import pyarrow.csv as pv
    import pyarrow.parquet as pq
    filename = get_filename(url)
    src_file = f"{path_to_local_home}/{filename}"
    if not src_file.endswith('.csv'):
        logging.error("Can only accept source files in CSV format, for the moment")
        return
    table = pv.read_csv(src_file)
    pq.write_table(table, src_file.replace('.csv', '.parquet'))


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # End of Workaround

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


default_args = {
    "owner": "airflow",
    "start_date": datetime(2022,4,1),
    "end_date":datetime(2022,12,31),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_ingestion_gcs_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:


    for url in github_url:
        parquet_file = get_filename(url).replace('.csv', '.parquet')
        table_name = get_filename(url).replace('.csv', '')
        download_dataset_task = PythonOperator(
            task_id=f"from_json_2_csv_task_{os.path.basename(urlparse(url).path)}",
            python_callable=from_json_2_csv,
            op_kwargs={
                "url": url,
                "path_to_local_home": path_to_local_home
            },
        )

        format_to_parquet_task = PythonOperator(
            task_id=f"format_to_parquet_task_{os.path.basename(urlparse(url).path)}",
            python_callable=format_to_parquet,
            op_kwargs={
                "url": url,
                "path_to_local_home": path_to_local_home,
            },
        )

        local_to_gcs_task = PythonOperator(
            task_id=f"local_to_gcs_task_{os.path.basename(urlparse(url).path)}",
            python_callable=upload_to_gcs,
            op_kwargs={
                "bucket": BUCKET,
                "object_name": f"{BUCKET_FOLDER}/{parquet_file}",
                "local_file": f"{path_to_local_home}/{parquet_file}",
            },
        )

        bigquery_external_table_task = BigQueryCreateExternalTableOperator(
            task_id=f"bigquery_external_table_task_{os.path.basename(urlparse(url).path)}",
            table_resource={
                "tableReference": {
                    "projectId": PROJECT_ID,
                    "datasetId": "raw",
                    "tableId": table_name,
                },
                "externalDataConfiguration": {
                    "sourceFormat": "PARQUET",
                    "sourceUris": [f"gs://{BUCKET}/{BUCKET_FOLDER}/{parquet_file}"],
                },
            },
        )

        download_dataset_task >> format_to_parquet_task >> local_to_gcs_task >> bigquery_external_table_task
