data "intersight_organization_organization" "org_details" {
  name = var.organization_name
}
resource "intersight_ntp_policy" "ntp1" {
  name        = "${var.prefix_for_policies}-ntp-policy"
  description = "NTP Policy for UCS Domain"
  enabled     = true
  ntp_servers = var.list_of_ntp_servers
  timezone    = var.timezone

organization {
  object_type = "organization.Organization"
  moid        = data.intersight_organization_organization.org_details.results[0].moid
  }
}