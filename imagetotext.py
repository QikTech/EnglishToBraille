import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCRtesseract.exe'
from PIL import Image

img = Image.open('text.png')
text = tess.image_to_string(img)
print(text)