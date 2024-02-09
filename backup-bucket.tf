resource "google_storage_bucket" "minecraft_backup" {
  name          = "minecraft-backup"
  location      = local.region
  project       = local.project
  storage_class = "COLDLINE"
  force_destroy = true

  uniform_bucket_level_access = true
}