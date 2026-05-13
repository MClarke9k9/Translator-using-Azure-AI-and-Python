import os


def main():
    required_vars = [
        "TRANSLATOR_KEY",
        "TRANSLATOR_ENDPOINT",
        "TRANSLATOR_REGION"
    ]

    missing_vars = []

    for var in required_vars:
        value = os.getenv(var)

        if value:
            if var == "TRANSLATOR_KEY":
                print(f"{var}: SET")
            else:
                print(f"{var}: {value}")
        else:
            missing_vars.append(var)
            print(f"{var}: MISSING")

    if missing_vars:
        print("\nMissing required environment variables:")
        for var in missing_vars:
            print(f"- {var}")
    else:
        print("\nTranslator configuration looks good.")


if __name__ == "__main__":
    main()