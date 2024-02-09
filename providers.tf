# We require a project to be provided upfront
# Create a project at https://cloud.google.com/
# Make note of the project ID
# We need a storage bucket created upfront too to store the terraform state
terraform {
  backend "gcs" {
    prefix = "terraform/state"
    bucket = "terraform-minecraft-server"
  }
}

provider "google" {
  project = local.project
  region  = local.region
}