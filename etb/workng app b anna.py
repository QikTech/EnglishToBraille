from flask import Flask, render_template, request, redirect
import pytesseract as tess
# Dom
tess.pytesseract.tesseract_cmd  = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image,ImageDraw, ImageFont
import os
from werkzeug.utils import secure_filename
from etb_package import alphaToBraille,brailleToAlpha, first
from fpdf import FPDF

# img= Image.open('text.png')
# text = tess.image_to_string(img)
# print (text)

app = Flask(__name__)

# WHERE TO STORE UPLOADED IMAGE
# Dom
path = app.config['IMAGE_UPLOADS'] = "C:/programming0.2/Mlai/EnglishToBraille/etb/static/image/uploads/"
# FILE VALIDATIONS 
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPEG","JPG"]

our_image = ""
uploaded_image = None
is_plaintext = False

@app.route('/')
def main():
     return render_template('app.html')

@app.route("/upload", methods=("GET", "POST"))
def upload_image():
     if request.files:
          image = request.files["image"]
          print(image)
          
          print("image:  "+str(image))
          if image.filename == "":
               print("image must have a name")
               return redirect(request.url)
          
          if not allowed_image(image.filename):
               print("that image is not valid (invalid image extension)")
               return redirect(request.url)

          else:
               filename = secure_filename(image.filename)
               # Handeling spacebar in Image Title
               lstr_img_name = str(image.filename).replace(" ", "_")
               image.save(os.path.join(app.config['IMAGE_UPLOADS'], lstr_img_name))
               # image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
          print(type(filename))
          print ('image saved ' + filename)
          global uploaded_image
          uploaded_image = filename
          print(uploaded_image)
          global our_image
          our_image = "/static/image/uploads/" + uploaded_image
          return redirect(request.url)          

     return render_template('app.html', uploaded = our_image)

def allowed_image(filename):
     if not "." in filename:
          return False
     
     ext= filename.rsplit(".",1)[1]

     if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
          return True
     else:
          return False

@app.route('/scan')
# def send():
def scan():
     a=200
     print("path"+str(path))
     print("uploaded_image"+str(uploaded_image))
     img= Image.open(path+uploaded_image,mode='r')
     # img= Image.open('etb/static/image/uploads',uploaded_image)
     plain_text = tess.image_to_string(img)
     # plain_text = ("kalpesh Ghangav")
     print (plain_text)
     # Package Working
     a= first.aaa

     # DISPLAY IMAGE
     global our_image
     # our_image = "/static/image/uploads/" + uploaded_image
     
     # -----------------------------------------------------------TESTER
     # braille = alphaToBraille.translate(plain_text)
     # print("text_scanned:\n"+plain_text)
     # print("text_translated:\n"+braille)

     # PDF GENERATION
     pdf = FPDF()
     pdf.add_page()
     pdf.set_font('Arial', '', 12)
     pdf.multi_cell(0, 4, str(plain_text))
     # pdf.ln()
     pdf.output('tuto1.pdf', 'F')

     #--------------------------------------------------------TXT GENERATION
     outfile = open('plain text.txt','w')
     outfile.write(plain_text)
     outfile.close()
     #--------------------------------------------------------TXT GENERATION END

     #--------------------------------------------------------TXT GENERATION
     new = Image.new('RGBA',(1080,1920),'white')
     # get a font
     fnt = ImageFont.truetype("roboto.ttf", 20)
     d = ImageDraw.Draw(new)
     d.multiline_text((100,100), str(plain_text), fill='black',font=fnt)
     new.save('Plain Text.png')
     #--------------------------------------------------------TXT GENERATION END
     
     # For braille Printing
     return render_template('app.html',pt=plain_text,uploaded=our_image)
     

@app.route('/braille_text',methods=['GET','POST'])
def show():
     #SamBam33 was here
     global is_plaintext
     is_plaintext = True
     if request.method == "POST":
          is_plaintext = False
          editedtext = request.form['changedtext']
          print("-------------------------------------------")
          print(editedtext)
     #SamBam33 left here

     a=200
     print("path"+str(path))
     print("uploaded_image"+str(uploaded_image))
     img= Image.open(path+uploaded_image,mode='r')
     # img= Image.open('etb/static/image/uploads',uploaded_image)
     plain_text = tess.image_to_string(img)
     # plain_text = ("kalpesh Ghangav")
     print (plain_text)
     # Package Working
     a= first.aaa
     
     braille = alphaToBraille.translate(plain_text)
     print (braille)
     # braille = alphaToBraille.translate(editedtext)
     # print("text_scanned:\n"+editedtext)
     # print("text_translated:\n"+braille)
     
     # #--------------------------------------------------------TXT GENERATION
     # outfile = open('plain text.txt','w')
     # outfile.write( braille )
     # outfile.close()
     # #--------------------------------------------------------TXT GENERATION END

     # #--------------------------------------------------------TXT GENERATION
     # new = Image.new('RGBA',(1080,1920),'white')
     # # get a font
     # fnt = ImageFont.truetype("SwellBraille.ttf", 20)
     # d = ImageDraw.Draw(new)
     # d.multiline_text((100,100), str(braille), fill='black',font=fnt)
     # new.save('Plain Text.png')
     # #--------------------------------------------------------TXT GENERATION END
      
     # For braille Printing
     return render_template('app.html', hop=a, t=braille, pt=plain_text, uploaded = our_image)
     # # For Plain Text Printing
     # return render_template('app.html', hop=a, t=plain_text)
     

# @app.route('/download_txt',methods=['GET','POST'])
# def download_txt():
#      outfile = open('plain text.txt','w')
#      outfile.write( plain_text )
#      outfile.close()
#      #--------------------------------------------------------TXT GENERATION END
#      return 

# @app.route('/download_img',methods=['GET','POST'])
# def download_image():
#      braille = show()
#      new = Image.new('RGBA',(1080,1920),'white')
#      # get a font
#      fnt = ImageFont.truetype("SwellBraille.ttf", 20)
#      d = ImageDraw.Draw(new)
#      d.multiline_text((100,100), str(braille), fill='black',font=fnt)
#      new.save('Plain Text.png')
#      #--------------------------------------------------------TXT GENERATION END