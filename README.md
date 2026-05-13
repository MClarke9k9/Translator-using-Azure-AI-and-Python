# Azure AI Translator with Python (CLI + SDK)
<img width="2805" height="1031" alt="AItranslator" src="https://github.com/user-attachments/assets/eb7fe3ce-1804-464d-b8fa-d25ddb226ec5" />

## Overview

This project demonstrates how to use **Azure AI Translator** with Python and Azure CLI to translate text programmatically.

It includes:

- Python translation scripts
- Azure CLI integration to retrieve credentials
- Environment variable-based authentication
- CLI-based custom translation tool

---

# Project Structure

```text
Translator-using-Azure-AI-and-Python/
│
├── text-translation-app.py
├── translate-custom-text.py
├── check-translator-config.py
├── requirements.txt
└── README.md
```

---

# Prerequisites

Install:

- Python 3
- Azure CLI
- Azure AI Translator resource (created via Terraform or Portal)

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

# Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Get Translator Credentials (Azure CLI)

Set variables:

```bash
RESOURCE_GROUP="rg_eastus_XXXXX"
TRANSLATOR_NAME="translator-demo-XXXXX"
```

Get endpoint:

```bash
az cognitiveservices account show \
  --name $TRANSLATOR_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "properties.endpoint" \
  --output tsv
```

Get region:

```bash
az cognitiveservices account show \
  --name $TRANSLATOR_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "location" \
  --output tsv
```

Get key:

```bash
az cognitiveservices account keys list \
  --name $TRANSLATOR_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "key1" \
  --output tsv
```

---

# Set Environment Variables

## macOS/Linux

```bash
export TRANSLATOR_KEY="<your-key>"
export TRANSLATOR_ENDPOINT="<your-endpoint>"
export TRANSLATOR_REGION="eastus"
```

## Windows PowerShell

```powershell
$env:TRANSLATOR_KEY="<your-key>"
$env:TRANSLATOR_ENDPOINT="<your-endpoint>"
$env:TRANSLATOR_REGION="eastus"
```

---

# Validate Configuration

```bash
python3 check-translator-config.py
```

Expected:

```text
TRANSLATOR_KEY: SET
TRANSLATOR_ENDPOINT: https://...
TRANSLATOR_REGION: eastus
```

---

# Run Default Translation App

```bash
python3 text-translation-app.py
```

Output:

```text
Text was translated to 'es' and the result is: Esta es una prueba
Text was translated to 'it' and the result is: Questo è un test
```

---

# Run Custom Translator CLI

```bash
python3 translate-custom-text.py \
  --text "Hello, this is my project" \
  --to es it fr
```

Output:

```text
es: Hola, este es mi proyecto
it: Ciao, questo è il mio progetto
fr: Bonjour, c'est mon projet
```

---


# Skills Demonstrated

- Azure AI Translator
- Python SDK usage
- Azure CLI integration
- Secure credential handling
- CLI tool development
- API interaction
- Error handling

