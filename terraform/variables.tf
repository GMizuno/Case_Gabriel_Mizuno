variable "project_id" {
  type    = string
  default = "case-445517"
}
variable "region" {
  type    = string
  default = "us-east1"
}

variable "service_account" {
  type = string
  default = "functions-case@case-445517.iam.gserviceaccount.com"
}

variable "bucket_trigger_transactions" {
  type=string
}

variable "function_name_transactions" {
  type = string
}

variable "origin_file_transactions" {
  type = string
}
