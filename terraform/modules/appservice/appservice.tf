resource random_pet "test"{}

resource "azurerm_service_plan" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  os_type             = "Windows"
  sku_name            = "B1"
}

resource "azurerm_windows_web_app" "test" {
  name                = "${var.application_type}-${var.resource_type}-${random_pet.test.id}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  service_plan_id     = azurerm_service_plan.test.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }
  site_config {
    always_on = false
  }
}

# sku size
# "F1",
# "P1V2",
# "P1V3",
# "B1"