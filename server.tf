# VM to run Minecraft, we use preemptable which will shutdown within 24 hours
resource "google_compute_instance" "minecraft" {
  name           = "minecraft-server"
  machine_type   = "e2-medium"
  project        = local.project
  zone           = local.zone
  enable_display = false
  tags           = ["minecraft", "http-server", "https-server"]
  labels = {
    "minecraft" = ""
  }
  metadata = {
    "enable-oslogin"  = "true"
    "startup-script"  = "screen -d -m -S mcs java -Xms1G -Xmx3G -jar /home/minecraft/minecraft_server.1.20.4.jar nogui"
    "shutdown-script" = <<-EOT
                #!/bin/bash
                /home/minecraft/backup.sh
                screen -r mcs -X stuff '/stop\n'
            EOT
  }

  service_account {
    email  = google_service_account.minecraft.email
    scopes = ["storage-rw"]
  }

  boot_disk {
    auto_delete = true
    device_name = "minecraft-server"
    initialize_params {
      size = 20
      type = "pd-balanced"
    }
  }

  network_interface {
    access_config {
      network_tier = "PRENIUM"
    }
  }

  scheduling {
    preemptible                 = true
    provisioning_model          = "SPOT"
    instance_termination_action = "STOP"
    automatic_restart           = false
  }

  timeouts {

  }

  lifecycle {
    ignore_changes = [network_interface, metadata] # Needed for metadata because of the syntax
  }
}
