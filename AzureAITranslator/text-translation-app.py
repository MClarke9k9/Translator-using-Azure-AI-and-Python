import os
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError


def main():
    key = os.getenv("TRANSLATOR_KEY")
    endpoint = os.getenv("TRANSLATOR_ENDPOINT")
    region = os.getenv("TRANSLATOR_REGION")

    if not key or not endpoint or not region:
        print("Missing environment variables.")
        print("Set TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, and TRANSLATOR_REGION.")
        return

    credential = TranslatorCredential(key, region)
    client = TextTranslationClient(endpoint=endpoint, credential=credential)

    try:
        source_language = "en"
        target_languages = ["es", "it"]
        text_to_translate = "This is a test"

        response = client.translate(
            content=[InputTextItem(text=text_to_translate)],
            to=target_languages,
            from_parameter=source_language
        )

        translation = response[0] if response else None

        if translation:
            for translated_text in translation.translations:
                print(
                    f"Text was translated to '{translated_text.to}' "
                    f"and the result is: {translated_text.text}"
                )

    except HttpResponseError as exception:
        print(f"Error Code: {exception.error.code}")
        print(f"Message: {exception.error.message}")


if __name__ == "__main__":
    main()