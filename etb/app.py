from flask import Flask, render_template, request, redirect
import pytesseract as tess
tess.pytesseract.tesseract_cmd  = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image,ImageDraw, ImageFont
import os
from werkzeug.utils import secure_filename
from etb_package import alphaToBraille,brailleToAlpha, first
from fpdf import FPDF

app = Flask(__name__)

# WHERE TO STORE UPLOADED IMAGE
# Dom
path = app.config['IMAGE_UPLOADS'] = "C:/programming0.2/Mlai/EnglishToBraille/etb/static/image/uploads/"
# FILE VALIDATIONS 
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPEG","JPG"]

our_image = ""
plain_text = None
braille = None
edited__text = None
braille2 = None
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
     # a=200
     # print("path"+str(path))
     # print("uploaded_image"+str(uploaded_image))
     img= Image.open(path+uploaded_image,mode='r')
     # img= Image.open('etb/static/image/uploads',uploaded_image)
     global plain_text
     plain_text = tess.image_to_string(img)
     # plain_text = ("kalpesh Ghangav")
     # print (plain_text)
     # Package Working
     # a= first.aaa

     # DISPLAY IMAGE
     # our_image = "/static/image/uploads/" + uploaded_image
     
     # -----------------------------------------------------------TESTER
     # braille = alphaToBraille.translate(plain_text)
     # print("text_scanned:\n"+plain_text)
     # print("text_translated:\n"+braille)

     # #------------------------------------------------------PDF GENERATION
     # pdf = FPDF()
     # pdf.add_page()
     # pdf.set_font('Arial', '', 12)
     # pdf.multi_cell(0, 4, str(plain_text))
     # # pdf.ln()
     # pdf.output('tuto1.pdf', 'F')

     # #--------------------------------------------------------TXT GENERATION
     # outfile = open('plain text.txt','w')
     # outfile.write(plain_text)
     # outfile.close()
     # #TXT GENERATION END

     # #--------------------------------------------------------PNG GENERATION
     # new = Image.new('RGBA',(1080,1920),'white')
     # # get a font
     # fnt = ImageFont.truetype("roboto.ttf", 20)
     # d = ImageDraw.Draw(new)
     # d.multiline_text((100,100), str(plain_text), fill='black',font=fnt)
     # new.save('Plain Text.png')
     # #TXT GENERATION END
     
     # For braille Printing
     global our_image
     return render_template('app.html',pt=plain_text,uploaded=our_image)
     

@app.route('/braille_text',methods=['POST'])
def show():
     #SamBam33 was here
     #SamBam33 left here
     edited__text = request.form['send__text']
     # print(edited__text)

     # a=200
     # print("path"+str(path))
     # print("uploaded_image"+str(uploaded_image))
     img= Image.open(path+uploaded_image,mode='r')
     # img= Image.open('etb/static/image/uploads',uploaded_image)
     plain_text = tess.image_to_string(img)
     # plain_text = ("kalpesh Ghangav")
     # print (plain_text)
     # Package Working
     # a= first.aaa
     global braille
     global braille2
     # braille = alphaToBraille.translate(plain_text)
     braille = alphaToBraille.translate(edited__text)
     braille2 = str(braille).replace("\n", "").replace("?", "")
     
     # print (braille)
  
     # For braille Printing
     return render_template('app.html', t=braille2, pt=edited__text, uploaded = our_image)

@app.route('/download_txt',methods=['GET','POST'])
def download_txt():
     global plain_text, braille, edited__text, braille2
     # print(plain_text,"-----------------")
     # print(type(plain_text))
     outfile = open('plain text.txt','w',encoding="utf-8")
     outfile.write( braille2 )
     outfile.close()
     return render_template('app.html', t=braille2, pt=plain_text, uploaded = our_image)

@app.route('/download_img',methods=['GET','POST'])
def download_image():
     global plain_text, braille, edited__text, braille2
     new = Image.new('RGBA',(1080,1920),'white')
     # get a font
     fnt = ImageFont.truetype("SwellBraille.ttf", 14)
     d = ImageDraw.Draw(new)
     d.multiline_text((60,60), braille, fill='black',font=fnt)
     new.save('Plain Text.png')
     return render_template('app.html', t=braille2, pt=plain_text, uploaded = our_image)

# @app.route('/download_pdf',methods=['GET','POST'])
# def download_pdf():
#      global plain_text, braille
#      # braille = braille.encode('latin-1', 'replace').decode("latin-1")
    
#      # braille = braille.encode("utf-8")
#      # print(type(braille))
#      # test_braille = braille.decode("utf-8")
#      # print("-------------------")
#      # print(test_braille)
#      # print(type(test_braille))

#      """
#      braille = braille.encode('latin-1')
#      print(braille + type(braille) + "Test type")
#      braille = braille.decode("utf-8")
#      print(braille + type(braille) + "UTF-8 Test")
#      """
#      pdf = FPDF()
#      pdf.add_font("NotoSans", style="", fname="NotoSans-Regular.ttf", uni=True)
#      pdf.add_font("NotoSans", style="B", fname="NotoSans-Bold.ttf", uni=True)
#      pdf.add_font("NotoSans", style="I", fname="NotoSans-Italic.ttf", uni=True)
#      pdf.add_font("NotoSans", style="BI", fname="NotoSans-BoldItalic.ttf", uni=True) 
#      pdf.add_page()
#      pdf.set_font('NotoSans', '', 12)  
#      pdf.multi_cell(0, 4, str(braille))
#      # pdf.ln()

#      pdf.output('plain text.pdf', 'F')
#      return render_template('app.html', t=braille, pt=plain_text, uploaded = our_image)