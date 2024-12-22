terraform {
  backend "gcs" {
    bucket = "gcp-case-terraform"
    prefix = "function"
  }
}