from flask import Flask, render_template, request
import pytesseract as tess
from PIL import Image

# img= Image.open('text.png')
# text = tess.image_to_string(img)
# print (text)

app = Flask(__name__)

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

     # else:
     #      return render_template('app.html')

     # if request.method == 'POST':
     #      num1 = request.form['num1']
     #      num2 = request.form['num2'] 
     #      operation = request.form['operation']

     # if operation == 'add':
     #      sum = float(num1) + float(num2)
     #      return render_template('app.html', sum=sum, hop=a, t=text)
     # elif operation == 'substraction':
     #      sum = float(num1) - float(num2)
     #      return render_template('app.html', sum=sum)
     # elif operation == 'multiply':
     #      sum = float(num1) * float(num2)
     #      return render_template('app.html', sum=sum)
     # elif operation == 'divide':
     #      sum = float(num1) / float(num2)
     #      return render_template('app.html', sum=sum)
     # else:
     #      return render_template('app.html')
     

    


     # @app.route('/hope')
     # def hope():
     #      return render_template("hope.html", hop=a)