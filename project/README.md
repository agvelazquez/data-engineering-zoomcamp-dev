# Data Engineering Zoomcamp project

## What's the project about?

**Ukraine humanitarian crisis.** The project will showcase an daily update of the consequences of the war in Ukraine. The idea is using this space to show the terrible consequences of the war with daily updates on the death toll and news. 

Using Python for data ingestion and Airflow for pipeline orchestation the infrastructure will consume death toll information for UN daily update, russian casualities from Kaggle dataset and news from Twitter. 

Information will be hosted in GCP and processed using SQL and DBT.   

The final output is a dashboard in Data Studio centralizing the information and updated daily. 

## Sources of information

* United Nations Human Rights website (https://www.ohchr.org/)
* Twitter (https://twitter.com/)
* Kaggle dataset (https://www.kaggle.com/datasets/piterfm/2022-ukraine-russian-war?select=russia_losses_equipment.csv)

### Technologies
* *Google Cloud Platform (GCP)*: Cloud-based auto-scaling platform by Google
  * *Google Cloud Storage (GCS)*: Data Lake
  * *BigQuery*: Data Warehouse
* *Terraform*: Infrastructure-as-Code (IaC)
* *Docker*: Containerization
* *SQL*: Data Analysis & Exploration
* *Airflow*: Pipeline Orchestration
* *dbt*: Data Transformation

### Project Diagram

<div align="center">
  <img src="https://github.com/agvelazquez/data-engineering-zoomcamp-dev/blob/main/project/project_diagram.svg"><br>
</div>


