from flask import Flask, render_template, request, redirect
import pytesseract as tess
from PIL import Image
import os
from werkzeug.utils import secure_filename
from base_braille import alphaToBraille, brailleToAlpha

# img= Image.open('text.png')
# text = tess.image_to_string(img)
# print (text)

app = Flask(__name__)

# WHERE TO STORE UPLOADED IMAGE
path = app.config['IMAGE_UPLOADS'] = "E:/Programming 0.1/MLai/Flask/English To Braille/etb/static/image/uploads/"
# FILE VALIDATIONS 
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPEG","JPG"]

uploaded_image = None

@app.route('/')
def main():
     return render_template('app.html')


@app.route("/upload", methods=("GET", "POST"))
def upload_image():
     if request.files:
          image = request.files["image"]
          print("image:  "+str(image))
          if image.filename == "":
               print("image must have a name")
               return redirect(request.url)
          
          if not allowed_image(image.filename):
               print("that image is not valid (invalid image extension)")
               return redirect(request.url)

          else:
               filename = secure_filename(image.filename)
               lstr_img_name = str(image.filename).replace(" ", "_")
               image.save(os.path.join(app.config['IMAGE_UPLOADS'], lstr_img_name))
          print ('image saved ' + filename)
          global uploaded_image
          uploaded_image = filename
          return redirect(request.url)          


     return render_template('app.html')

def allowed_image(filename):
     if not "." in filename:
          return False
     
     ext= filename.rsplit(".",1)[1]

     if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
          return True
     else:
          return False

@app.route('/send')
# def send():
def show():
     a=200
     print("path"+str(path))
     print("uploaded_image"+str(uploaded_image))
     img= Image.open(path+uploaded_image,mode='r')
     # img= Image.open('etb/static/image/uploads',uploaded_image)
     plain_text = tess.image_to_string(img)
     # plain_text = ("kalpesh Ghangav")
     print (plain_text)
     return render_template('app.html', hop=a, t=plain_text)
     braille = etb.base_braille.alphaToBraille.translate(plain_text)
     print("text_translated:\n"+braille)

     

