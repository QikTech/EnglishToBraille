@app.route('/braille_text',methods=['GET','POST'])
def show():
 a=200
     print("path"+str(path))
     print("uploaded_image"+str(uploaded_image))
     img= Image.open(path+uploaded_image,mode='r')
     plain_text = tess.image_to_string(img)
     print (plain_text)
     a= first.aaa
     braille = alphaToBraille.translate(plain_text)
     # this braille Variable i want in following function
     return render_template('app.html', hop=a, t=braille, pt=plain_text, uploaded = our_image)


@app.route('/download_img',methods=['GET','POST'])
def download_image():
     new = Image.new('RGBA',(1080,1920),'white')
     fnt = ImageFont.truetype("SwellBraille.ttf", 20)
     d = ImageDraw.Draw(new)
     d.multiline_text((100,100), str(braille), fill='black',font=fnt)
     # Variable call here
     new.save('Plain Text.png')
     return render_template('app.html')