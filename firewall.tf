# Open the firewall for Minecraft traffic
resource "google_compute_firewall" "minecraft" {
  name    = "minecraft"
  network = data.google_compute_network.default.id

  priority = 500
  # Minecraft client port
  allow {
    protocol = "tcp"
    ports    = ["25565"]
  }
  # ICMP (ping)
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "udp"
    ports    = ["19132"]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["minecraft"]
}

data "google_compute_network" "default" {
  name = "default"
}