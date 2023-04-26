provider "google" {
  region  = "us-central1"
}

module "kubernetes-engine_example_simple_autopilot_private" {
  source  = "terraform-google-modules/kubernetes-engine/google//examples/simple_autopilot_private"
  version = "25.0.0"
  project_id = "playground-s-11-6bf8c365"
  region  = "us-central1"
}
 