# Azure GUIDS
variable "subscription_id" {}
variable "client_id" {}
variable "client_secret" {}
variable "tenant_id" {}

# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "application_type" {}

# Network
variable "virtual_network_name" {}
variable "address_prefixes_test" {}
variable "address_space" {}

# VM
variable "admin_username" {
  default = "realadmin"
}
variable "vm_size" {
  default = "Standard_DS2_v2"
  # "Standard_B1s",
  # "Standard_B2s",
  # "Standard_DS1_v2",
  # "Standard_DS2_v2",
  # "Standard_D2s_v3",
  # "Standard_B2ms"
}
variable "vm_name" {
  default = "test"
}
# Udacity environment
variable "udacity_lab" {
  default = true
}

# Backend storage
variable "backend_storage_account_name" {}
variable "backend_container_name" {}
variable "backend_key" {}
variable "backend_access_key" {}

# SSH key
variable ssh_key_public {}