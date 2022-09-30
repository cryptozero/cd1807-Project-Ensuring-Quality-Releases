resource "azurerm_resource_group" "test" {
  count    = var.udacity_lab ? 0 : 1
  name     = var.resource_group
  location = var.location
}
