variable "resource_group_name" {
  description = "Existing Azure resource group name"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}

variable "name_suffix" {
  description = "Short suffix for globally unique resource names"
  type        = string
  default     = "mark"
}