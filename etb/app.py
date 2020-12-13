from flask import Flask, render_template, request, redirect
import pytesseract as tess
from PIL import Image
import os

# img= Image.open('text.png')
# text = tess.image_to_string(img)
# print (text)

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "E:/Programming 0.1/MLai/Flask/English To Braille/etb/static/image/uploads"
@app.route('/')
def main():
     return render_template('app.html')

@app.route('/send')
# def send():
def show():
     a=200
     img= Image.open('text.png')
     text = tess.image_to_string(img)
     print (text)
     return render_template('app.html', hop=a, t=text)


@app.route("/upload", methods=("GET", "POST"))
def upload_image():
     if request.files:
          image = request.files["image"]
          image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
          print ('image saved')
          return redirect(request.url)


     return render_template('app.html')