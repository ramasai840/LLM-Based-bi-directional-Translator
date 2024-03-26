from langdetect import detect
from googletrans import Translator

def translate_text(text, target_language = 'en'):
    detected_lang = detect(text)

    translator = Translator()
    translated_text = translator.translate(text, src = detected_lang, dest = target_language)


    return translated_text


input_text = "Ру́сский медве́дь"
output_text = translate_text(input_text, target_language='en')

print(output_text)