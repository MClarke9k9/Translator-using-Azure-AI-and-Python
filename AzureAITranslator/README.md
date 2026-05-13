# Files Explained

---

## `text-translation-app.py`

Simple script that:

- Translates hardcoded text
- Uses environment variables
- Demonstrates basic SDK usage

---

## `translate-custom-text.py`

Advanced CLI tool:

- Accepts dynamic input text
- Supports multiple languages
- Uses argparse for CLI input

Example:

```bash
python3 translate-custom-text.py --text "Hello world" --to es fr
```

---

## `check-translator-config.py`

Utility script to:

- Validate environment variables
- Prevent runtime errors
- Debug configuration issues

---

## `requirements.txt`

```text
azure-ai-translation-text==1.0.0b1
azure-core
```

---

# Common Language Codes

```text
es = Spanish
it = Italian
fr = French
de = German
pt = Portuguese
ja = Japanese
ko = Korean
```

---

# Troubleshooting

## Missing Environment Variables

Run:

```bash
python3 check-translator-config.py
```

---

## Authentication Errors

Verify:

- Key is correct
- Endpoint is correct
- Region matches resource

---

## Package Errors

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# Cleanup

Deactivate environment:

```bash
deactivate
```

---
