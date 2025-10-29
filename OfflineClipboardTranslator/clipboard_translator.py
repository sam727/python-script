# import pyperclip
# import argostranslate.package, argostranslate.translate

# # Setup language pair once
# installed_languages = argostranslate.translate.get_installed_languages()
# from_lang = next(lang for lang in installed_languages if lang.code == "en")
# to_lang = next(lang for lang in installed_languages if lang.code == "ko")

# # Translate from clipboard
# text = pyperclip.paste()
# translated = from_lang.get_translation(to_lang).translate(text)
# print("Translated:", translated)



import pyperclip
import argostranslate.package, argostranslate.translate

# Load installed languages
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = next(lang for lang in installed_languages if lang.code == "en")
to_lang = next(lang for lang in installed_languages if lang.code == "es")

# Read from clipboard
text = pyperclip.paste()
print(f"Original: {text}")

# Translate
translation = from_lang.get_translation(to_lang)
translated = translation.translate(text)

# Output + copy back to clipboard
print(f"Translated: {translated}")
pyperclip.copy(translated)
print("Translation copied to clipboard!")
