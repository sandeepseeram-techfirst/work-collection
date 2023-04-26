

resource "google_container_cluster" "my_cluster" {
  name               = "my-cluster"
  location           = "us-central1"
  remove_default_node_pool = true

  # Autopilot mode
  release_channel {
    channel = "autopilot"
  }

  # Private cluster
  private_cluster_config {
    enable_private_nodes = true
    enable_private_endpoint = true
    master_ipv4_cidr_block = "172.16.0.0/28"
  }

  # Labels
  labels = {
    env = "dev-qa"
  }
}