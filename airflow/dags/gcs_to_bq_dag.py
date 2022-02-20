import os
import logging

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
<<<<<<< Updated upstream

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'trips_data_all')

DATASET = "tripdata"
COLOUR_RANGE = {'yellow': 'tpep_pickup_datetime', 'green': 'lpep_pickup_datetime'}
INPUT_PART = "raw"
INPUT_FILETYPE = "parquet"
=======
from datetime import datetime

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = 'dtc-de-course-338720'

>>>>>>> Stashed changes

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}

<<<<<<< Updated upstream
# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="gcs_2_bq_dag",
=======
with DAG(
    dag_id="gcs_to_bq_dag",
>>>>>>> Stashed changes
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:

<<<<<<< Updated upstream
    for colour, ds_col in COLOUR_RANGE.items():
        move_files_gcs_task = GCSToGCSOperator(
            task_id=f'move_{colour}_{DATASET}_files_task',
            source_bucket=BUCKET,
            source_object=f'{INPUT_PART}/{colour}_{DATASET}*.{INPUT_FILETYPE}',
            destination_bucket=BUCKET,
            destination_object=f'{colour}/{colour}_{DATASET}',
            move_object=True
        )

        bigquery_external_table_task = BigQueryCreateExternalTableOperator(
            task_id=f"bq_{colour}_{DATASET}_external_table_task",
=======
    gcs_2_gsc = GCSToGCSOperator(
        task_id='gcs_2_gsc',
        source_bucket=BUCKET,
        source_object=f'{BUCKET}/raw/yellow_tripdata_*.parquet',
        destination_bucket=BUCKET,
        destination_object='yellow/'
    )

    gcs_2_bq_ext = BigQueryCreateExternalTableOperator(
            task_id="gcs_2_bq_ext",
>>>>>>> Stashed changes
            table_resource={
                "tableReference": {
                    "projectId": PROJECT_ID,
                    "datasetId": BIGQUERY_DATASET,
<<<<<<< Updated upstream
                    "tableId": f"{colour}_{DATASET}_external_table",
                },
                "externalDataConfiguration": {
                    "autodetect": "True",
                    "sourceFormat": f"{INPUT_FILETYPE.upper()}",
                    "sourceUris": [f"gs://{BUCKET}/{colour}/*"],
                },
            },
        )

        CREATE_BQ_TBL_QUERY = (
            f"CREATE OR REPLACE TABLE {BIGQUERY_DATASET}.{colour}_{DATASET} \
            PARTITION BY DATE({ds_col}) \
            AS \
            SELECT * FROM {BIGQUERY_DATASET}.{colour}_{DATASET}_external_table;"
        )

        # Create a partitioned table from external table
        bq_create_partitioned_table_job = BigQueryInsertJobOperator(
            task_id=f"bq_create_{colour}_{DATASET}_partitioned_table_task",
            configuration={
                "query": {
                    "query": CREATE_BQ_TBL_QUERY,
                    "useLegacySql": False,
                }
            }
        )

        move_files_gcs_task >> bigquery_external_table_task >> bq_create_partitioned_table_job
=======
                    "tableId": "external_yellow_tripdata_airflow",
                },
                "externalDataConfiguration": {
                    "autodetect":"True",    
                    "sourceFormat": "PARQUET",
                    "sourceUris": [f"gs://{BUCKET}/yellow/*"],
                },
            },
    )

    CREATE_PART_TBL_QUERY = \
    f"""
        CREATE OR REPLACE TABLE {BIGQUERY_DATASET}.nytaxi.yellow_tripdata_airflow
        PARTITION BY DATE(tpep_pickup_datetime)
        CLUSTER BY VendorID AS
        SELECT * FROM {BIGQUERY_DATASET}.nytaxi.external_yellow_tripdata_airflow;
    """

    bq_ext_2_bq_part = BigQueryInsertJobOperator(
        task_id="bq_ext_2_bq_part",
        configuration={
            "query": {
                "query": CREATE_PART_TBL_QUERY,
                "useLegacySql": False,
            }
        },
    )    



gcs_2_gsc >> gcs_2_bq_ext >> bq_ext_2_bq_part 
>>>>>>> Stashed changes
