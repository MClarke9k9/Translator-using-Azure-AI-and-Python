import os
import argparse
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError


def translate_text(text, source_language, target_languages):
    key = os.getenv("TRANSLATOR_KEY")
    endpoint = os.getenv("TRANSLATOR_ENDPOINT")
    region = os.getenv("TRANSLATOR_REGION")

    if not key or not endpoint or not region:
        raise EnvironmentError(
            "Set TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, and TRANSLATOR_REGION."
        )

    credential = TranslatorCredential(key, region)
    client = TextTranslationClient(endpoint=endpoint, credential=credential)

    response = client.translate(
        content=[InputTextItem(text=text)],
        to=target_languages,
        from_parameter=source_language
    )

    return response[0].translations if response else []


def main():
    parser = argparse.ArgumentParser(description="Translate text using Azure AI Translator.")
    parser.add_argument("--text", required=True, help="Text to translate.")
    parser.add_argument("--from-lang", default="en", help="Source language code.")
    parser.add_argument(
        "--to",
        nargs="+",
        default=["es", "it"],
        help="Target language codes. Example: --to es it fr"
    )

    args = parser.parse_args()

    try:
        translations = translate_text(args.text, args.from_lang, args.to)

        for item in translations:
            print(f"{item.to}: {item.text}")

    except HttpResponseError as exception:
        print(f"Error Code: {exception.error.code}")
        print(f"Message: {exception.error.message}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()