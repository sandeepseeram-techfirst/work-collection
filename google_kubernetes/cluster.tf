resource "google_container_cluster" "cluster-autopilot" {
  provider = google-beta

  name            = "cluster-autopilot"
  description     = "Testing Terraform for GKE-Autopilot"
  project         = "playground-s-11-3b84b43b"

  location        = "us-central1"

  network         = "default"

  subnetwork      = "default"

  enable_autopilot = true
  
  ip_allocation_policy {
  }

}