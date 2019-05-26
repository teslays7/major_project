from flask import Flask, request, render_template, redirect, url_for, flash
from recognize_faces_image import testing_func 
from encode_faces import start_encoding 
from werkzeug.utils import secure_filename
import os

# UPLOAD_FOLDER = 'dataset'

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/register')
def register_page():
    return render_template('registerpage.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    imagename = request.form['imagename']
    imagefile = request.files.get('imagefile', '')
    filename = secure_filename(imagefile.filename)
    flash('file saved')
    newpath='dataset/' + imagename
    print(newpath)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    imagefile.save(os.path.join(newpath, filename))
    return render_template('registerpage.html')

@app.route('/train')
def training():
    start_encoding()
    return render_template('homepage.html')

@app.route('/test')
def upload_testing():
    return render_template('testpage.html')

@app.route('/recognize', methods=['POST'])
def recognize_image():
    imagefile = request.files.get('imagefile', '')
    filename = secure_filename(imagefile.filename)
    flash('file saved')
    newpath='examples'
    imagefile.save(os.path.join(newpath, filename))
    name=testing_func('examples/'+filename)
    return ('The kid recognized in the sent pic is ' + name)

if __name__ == '__main__':
    app.run(debug = True)
