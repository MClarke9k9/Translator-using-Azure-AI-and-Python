data "azurerm_resource_group" "rg" {
  name = var.resource_group_name
}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

resource "azurerm_cognitive_account" "translator" {
  name                = "translator-demo-${var.name_suffix}-${random_string.suffix.result}"
  location            = data.azurerm_resource_group.rg.location
  resource_group_name = data.azurerm_resource_group.rg.name

  kind     = "CognitiveServices"
  sku_name = "S0"

  custom_subdomain_name = "translator-demo-${var.name_suffix}-${random_string.suffix.result}"

  identity {
    type = "SystemAssigned"
  }
}