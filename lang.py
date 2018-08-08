from PIL import Image
from pytesseract import image_to_string
from langdetect import detect
from translate import translator


im = Image.open(r'/Users/gokul-6650/Desktop/french.png')
print(im)
print(image_to_string(im))

text = image_to_string(im)
print(detect(text))
language = "en"
lang = detect(text)


if lang != language:
    translatedText = translator(lang,language,text)
    print(translatedText)
