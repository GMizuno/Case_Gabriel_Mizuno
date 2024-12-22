module "gcs_functions" {
 source       = "./modules/storage-bucket"
}

module "cloud_functions_transactions" {
 source = "./modules/cloudfunction"
 bucket_name =  module.gcs_functions.gcs-name.name
 project_id = var.project_id
 region = var.region
 service_account = var.service_account
 function_name = var.function_name_transactions
 origin = var.origin_file_transactions
 bucket_trigger = var.bucket_trigger_transactions
}


