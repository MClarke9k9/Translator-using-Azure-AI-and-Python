# Install Terraform

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

Verify:

```bash
terraform version
```

---

# Install Azure CLI

```bash
brew install azure-cli
```

Login:

```bash
az login
```

---

# Terraform Configuration

This project creates:

- Azure AI Services multi-service account
- Translator capability (via Cognitive Services)
- System-assigned identity
- Secure access keys

---

# Deployment Steps

## Step 1: Navigate to Terraform Folder

```bash
cd terraform
```

---

## Step 2: Initialize Terraform

```bash
terraform init
```

---

## Step 3: Format Code

```bash
terraform fmt
```

---

## Step 4: Validate Configuration

```bash
terraform validate
```

---

## Step 5: Create Execution Plan

```bash
terraform plan \
-var="resource_group_name=rg_eastus_XXXXX"
```

---

## Step 6: Deploy Resources

```bash
terraform apply \
-var="resource_group_name=rg_eastus_XXXXX"
```

Type:

```text
yes
```

when prompted.

---

# Resources Created

## Azure AI Services Resource

- Type: Multi-service Cognitive Services
- SKU: Standard S0
- Region: East US
- Translator enabled

---

# Retrieve Outputs

View all outputs:

```bash
terraform output
```

---

## Get Translator Endpoint

```bash
terraform output translator_endpoint
```

---

## Get Translator Region

```bash
terraform output translator_location
```

---

## Get Translator Key

```bash
terraform output translator_key_1
```

---

# Connect to Python App

Export values as environment variables:

## macOS/Linux

```bash
export TRANSLATOR_KEY=$(terraform output -raw translator_key_1)
export TRANSLATOR_ENDPOINT=$(terraform output -raw translator_endpoint)
export TRANSLATOR_REGION=$(terraform output -raw translator_location)
```

---

## Windows PowerShell

```powershell
$env:TRANSLATOR_KEY = (terraform output -raw translator_key_1)
$env:TRANSLATOR_ENDPOINT = (terraform output -raw translator_endpoint)
$env:TRANSLATOR_REGION = (terraform output -raw translator_location)
```

---

# Test Integration

Run Python app:

```bash
python3 text-translation-app.py
```

---

# Expected Result

```text
Text was translated to 'es' and the result is: Esta es una prueba
Text was translated to 'it' and the result is: Questo è un test
```

---
