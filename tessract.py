import pytesseract as tess
tess.pytesseract.tesseract_cmd  = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img= Image.open('text.png')
text = tess.image_to_string(img)
print (text)

from PIL import Image, ImageDraw
text
new=Image.new('RGB', (500,500),color=(192,192,192))
d=ImageDraw.Draw(new)
d.text((100,100),text,fill=(255,255,255))
new.save('FirstHope1.png')