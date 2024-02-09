resource "google_storage_bucket" "minecraft_cloud_function_bucket" {
  name          = format("%s-minecraft-cloud-functions", local.project)
  location      = local.region
  project       = local.project
  force_destroy = true

  uniform_bucket_level_access = true
}

// -------- START FUNCTION --------
resource "google_storage_bucket_object" "minecraft_start_function" {
  name   = "minecraft-start-function.py.zip"
  bucket = google_storage_bucket.minecraft_cloud_function_bucket.name
  source = "./start-server-function-python/main.py.zip"
}

resource "google_cloudfunctions_function" "minecraft_start_function" {
  name        = "start-minecraft-server"
  description = "Cloud function that start the minecraft server & returns an HTML page with the server IP"
  runtime     = "python38"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.minecraft_cloud_function_bucket.name
  source_archive_object = google_storage_bucket_object.minecraft_start_function.name
  trigger_http          = true
  entry_point           = "main"

  service_account_email = google_service_account.minecraft.email
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = local.project
  region         = local.region
  cloud_function = google_cloudfunctions_function.minecraft_start_function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}


// -------- STOP FUNCTION --------

resource "google_storage_bucket_object" "minecraft_stop_function" {
  name   = "minecraft-stop-function.py.zip"
  bucket = google_storage_bucket.minecraft_cloud_function_bucket.name
  source = "./stop-server-function-python/main.py.zip"
}

resource "google_cloudfunctions_function" "minecraft_stop_function" {
  name        = "stop-minecraft-server"
  description = "Cloud function that stop the minecraft server & returns an HTML page with the server IP"
  runtime     = "python38"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.minecraft_cloud_function_bucket.name
  source_archive_object = google_storage_bucket_object.minecraft_stop_function.name
  trigger_http          = true
  entry_point           = "StopVM"

  service_account_email = google_service_account.minecraft.email
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = local.project
  region         = local.region
  cloud_function = google_cloudfunctions_function.minecraft_stop_function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}