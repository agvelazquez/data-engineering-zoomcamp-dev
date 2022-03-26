terraform {
  required_version = ">= 1.0"
  backend "local" {} # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.region
  zone        = var.zone
  credentials = file(var.credentials) # Use this if you do not want to set env-var GOOGLE_APPLICATION_CREDENTIALS
}

# Data Lake Bucket
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket
resource "google_storage_bucket" "data-lake-bucket" {
  name     = "${local.data_lake_bucket}_${var.project}" # Concatenating DL bucket & Project name for unique naming
  location = var.region

  # Optional, but recommended settings:
  storage_class               = var.storage_class
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 60 // days
    }
  }

  force_destroy = true
}

resource "google_storage_bucket_object" "content_folder_twitter" {
  name    = "twitter/"
  content = "Empty folder for Twitter data"
  bucket  = google_storage_bucket.data-lake-bucket.name
}

resource "google_storage_bucket_object" "content_folder_un" {
  name    = "un/"
  content = "Empty folder for United Nations data"
  bucket  = google_storage_bucket.data-lake-bucket.name
}

resource "google_storage_bucket_object" "content_folder_github" {
  name    = "github/"
  content = "Empty folder for Github data"
  bucket  = google_storage_bucket.data-lake-bucket.name
}

# DWH
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "dataset_1" {
  dataset_id = var.BQ_DATASET_1
  project    = var.project
  location   = var.region
}

resource "google_bigquery_dataset" "dataset_2" {
  dataset_id = var.BQ_DATASET_2
  project    = var.project
  location   = var.region
}

resource "google_bigquery_dataset" "dataset_3" {
  dataset_id = var.BQ_DATASET_3
  project    = var.project
  location   = var.region
}
