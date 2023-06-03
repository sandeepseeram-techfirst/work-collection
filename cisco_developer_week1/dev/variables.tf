variable "prefix_for_policies" {
  type        = string
  description = "Prefix to append for all the policies"
}

variable "organization_name" {
  type        = string
  description = "Organization to which policy belong"
}

variable "list_of_ntp_servers" {
  type        = list(any)
  description = "List of NTP Servers"
}

variable "timezone" {
  type        = string
  description = "TimeZone"
}