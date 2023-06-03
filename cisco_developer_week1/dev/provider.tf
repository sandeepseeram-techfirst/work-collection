terraform {
  required_providers {
    intersight = {
      source  = "CiscoDevNet/intersight"
      version = "1.0.32"
    }
  }
}
provider "intersight" {
  # Configuration options
  apikey    = "REPLACE-WITH-YOUR-ASSIGNED-GUEST-KEY"
  secretkey = "REPLACE-WITH-LOCATION-OF-YOUR-SECRET-KEY"
  endpoint  = "https://tme-demo.intersight.com"
}