## Data Engineering Zoomcamp course

**Hosted by https://datatalks.club/**

- **Start**: 17 January 2022
- The videos are published to [DataTalks.Club's YouTube channel](https://www.youtube.com/c/DataTalksClub) in [the course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb) 

## Folders
- **course**: Scripts of different tools built for some of the homeworks.
- **project**: Final project structure and repository.


## Course Syllabus

### Week 1: Introduction & Prerequisites

* Course overview
* Introduction to GCP
* Docker and docker-compose 
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course
* Homework


### Week 2: Data ingestion

* Data Lake
* Workflow orchestration
* Setting up Airflow locally
* Ingesting data to GCP with Airflow
* Ingesting data to local Postgres with Airflow
* Moving data from AWS to GCP (Transfer service)
* Homework


### Week 3: Data Warehouse

Goal: Structuring data into a Data Warehouse

Instructor: Ankush

* Data warehouse (BigQuery) (25 minutes)
    * What is a data warehouse solution
    * What is big query, why is it so fast, Cost of BQ,  (5 min)
    * Partitoning and clustering, Automatic re-clustering (10 min)
    * Pointing to a location in google storage (5 min)
    * Loading data to big query & PG (10 min) -- using Airflow operator?
    * BQ best practices
    * Misc: BQ Geo location, BQ ML 
    * Alternatives (Snowflake/Redshift)

Duration: 1-1.5h


### Week 4: Analytics engineering

Goal: Transforming Data in DWH to Analytical Views

Instructor: Victoria

* Basics of analytics engineering (15 mins)
* Developing a dbt project (Combination of coding + theory) (1:30)
* Visualising the data in Google data studio (15 mins)

Duration: 2h    


### Week 5: Batch processing

Goal: 

Instructor: Alexey

* Distributed processing (Spark) (40 + ? minutes)
    * What is Spark, spark cluster (5 mins)
    * Explaining potential of Spark (10 mins)
    * What is broadcast variables, partitioning, shuffle (10 mins)
    * Pre-joining data (10 mins)
    * use-case
    * What else is out there (Flink) (5 mins)
* Extending Orchestration env (airflow) (30 minutes)
    * Big query on airflow (10 mins)
    * Spark on airflow (10 mins)

Duration: 1-1.5h

### Week 6: Streaming

Goal: 

Instructor: Ankush

* Basics
    * What is Kafka
    * Internals of Kafka, broker
    * Partitoning of Kafka topic
    * Replication of Kafka topic
* Consumer-producer
* Schemas (avro)
* Streaming
    * Kafka streams
* Kafka connect
* Alternatives (PubSub/Pulsar)

Duration: 1.5h



### Week 7, 8 & 9: Project

* Putting everything we learned to practice

Duration: 2-3 weeks

* Upcoming buzzwords
  *  Delta Lake/Lakehouse
    * Databricks
    * Apache iceberg
    * Apache hudi
  * Data mesh
  * KSQLDB
  * Streaming analytics
  * Mlops
  
Duration: 30 mins


### Technologies
* *Google Cloud Platform (GCP)*: Cloud-based auto-scaling platform by Google
  * *Google Cloud Storage (GCS)*: Data Lake
  * *BigQuery*: Data Warehouse
* *Terraform*: Infrastructure-as-Code (IaC)
* *Docker*: Containerization
* *SQL*: Data Analysis & Exploration
* *Airflow*: Pipeline Orchestration
* *DBT*: Data Transformation
* *Spark*: Distributed Processing
* *Kafka*: Streaming



## Instructors

- Ankush Khanna (https://linkedin.com/in/ankushkhanna2)
- Sejal Vaidya (https://linkedin.com/in/vaidyasejal)
- Victoria Perez Mola (https://www.linkedin.com/in/victoriaperezmola/)
- Alexey Grigorev (https://linkedin.com/in/agrigorev)
