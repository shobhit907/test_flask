from flask import Flask,render_template,request
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os
from PIL import Image
import makePrediction

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# UPLOAD_FOLDER='../tmp/'
UPLOAD_FOLDER='./uploads/'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/welcome/',methods=["GET","POST"])
def welcome_screen():
    name=""
    print(request.form['username'])
    if(request.method=='POST'):
        name=request.form['username']
    return render_template('welcome.html',username=name)



@app.route('/image-detail/',methods=["POST"])
def image_detail():
    if(request.method=="POST"):
        file=request.files['image_file']
        filename=file.filename
        if(secure_filename(filename) and allowed_file(filename)):
            path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(path)
            file.save(path)
            img=Image.open(path)
            return render_template('imageDetail.html',image_detail=str(img.size))
            return str(img.size)
            return filename
        else:
            return "Invalid"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict/',methods=["POST"])
def predict_digit():
    if(request.method=="POST"):
        file=request.files['image_digit']
        filename=file.filename
        if(secure_filename(filename) and allowed_file(filename)):
            path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(path)
            file.save(path)
            return makePrediction.predict(path)
        else:
            return "Invalid"

if __name__=='__main__':
    app.run(debug=True,host="127.0.0.1",port=8000)
    