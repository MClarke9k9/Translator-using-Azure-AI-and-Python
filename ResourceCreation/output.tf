output "translator_resource_name" {
  value = azurerm_cognitive_account.translator.name
}

output "translator_location" {
  value = azurerm_cognitive_account.translator.location
}

output "translator_endpoint" {
  value = azurerm_cognitive_account.translator.endpoint
}

output "translator_key_1" {
  value     = azurerm_cognitive_account.translator.primary_access_key
  sensitive = true
}

output "translator_key_2" {
  value     = azurerm_cognitive_account.translator.secondary_access_key
  sensitive = true
}