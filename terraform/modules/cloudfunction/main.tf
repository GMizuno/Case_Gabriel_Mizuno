data "archive_file" "source" {
  type        = "zip"
  source_dir  = "../jobs/${var.origin}"
  output_path = "${path.module}/source/function_${var.origin}.zip"
}

resource "google_storage_bucket_object" "source_zip" {
  source       = data.archive_file.source.output_path
  content_type = "application/zip"
  name         = "source_${var.function_name}_zip-${data.archive_file.source.output_md5}.zip"
  bucket       = var.bucket_name
}

resource "google_cloudfunctions2_function" "cloud_functions" {
  name        = var.function_name
  description = "Cloud-function will get trigger once file is uploaded in input-${var.project_id}"
  project     = var.project_id
  location    = var.region

  build_config {
    runtime     = "python312"
    entry_point = "main"
    source {
      storage_source {
        bucket = var.bucket_name
        object = google_storage_bucket_object.source_zip.name
      }
    }
  }

  service_config {
    max_instance_count    = 1
    available_memory      = "512M"
    timeout_seconds       = 60
    service_account_email = var.service_account
  }

  event_trigger {
    trigger_region        = var.region
    event_type            = "google.cloud.storage.object.v1.finalized"
    service_account_email = var.service_account
    event_filters {
      attribute = "bucket"
      value     = var.bucket_trigger
    }
  }
}
