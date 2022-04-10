locals {
  data_lake_bucket = "de_project_dl"
}

variable "project" {
  description = "Your GCP project ID"
  default     = "de-course-project"
  type        = string
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "us-central1"
  type        = string
}

variable "zone" {
  description = "Zone for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "us-central1-a"
  type        = string
}

variable "credentials" {
  description = "Path for to the credentials json file"
  default     = "../.google/credentials/de-course-project-credentials.json"
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "STANDARD"
}

variable "BQ_DATASET_1" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type        = string
  default     = "raw"
}

variable "BQ_DATASET_2" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type        = string
  default     = "etl"
}

variable "BQ_DATASET_3" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type        = string
  default     = "agg"
}