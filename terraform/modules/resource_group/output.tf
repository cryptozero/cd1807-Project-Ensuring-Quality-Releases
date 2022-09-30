output "resource_group_name" {
  value = var.udacity_lab ? var.resource_group : "${azurerm_resource_group.test[0].name}"
}
