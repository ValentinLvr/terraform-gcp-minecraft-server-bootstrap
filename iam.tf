
# Create service account to run service with no permissions
resource "google_service_account" "minecraft" {
  account_id   = "minecraft"
  display_name = "minecraft"
  project      = local.project
  description  = "Can start/stop the minecraft server VM"
}

resource "google_compute_instance_iam_member" "minecraft_server_admin" {
  project       = local.project
  zone          = local.zone
  instance_name = google_compute_instance.minecraft.name
  role          = "roles/compute.instanceAdmin.v1"
  member        = format("serviceAccount:%s", google_service_account.minecraft.email)
}

resource "google_service_account_iam_member" "minecraft" {
  service_account_id = google_service_account.minecraft.name
  role               = "roles/iam.serviceAccountUser"
  member             = format("serviceAccount:%s", google_service_account.minecraft.email)
}

resource "google_storage_bucket_iam_member" "minecraft_backup" {
  bucket = google_storage_bucket.minecraft_backup.name
  role   = "roles/storage.admin"
  member = format("serviceAccount:%s", google_service_account.minecraft.email)
}