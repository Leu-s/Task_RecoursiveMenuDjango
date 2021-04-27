from slugify import slugify
from transliterate import translit, exceptions


def slugify_function(text: str):
    try:
        text = translit(text, reversed=True)
    except exceptions.LanguageDetectionError as error:
        print(error)
    return slugify(text)
