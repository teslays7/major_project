from flask import request, render_template, redirect, flash
from majorproject.recognize_faces_image import testing_func 
from majorproject.encode_faces import start_encoding 
from werkzeug.utils import secure_filename
import os, shutil, glob
from majorproject.models import Child
from majorproject import app
from majorproject.forms import RegistrationForm
from werkzeug.datastructures import CombinedMultiDict
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/register')
def register_page():
    form = RegistrationForm()
    return render_template('registerpage.html',form=form)

@app.route('/upload', methods=['POST'])
def upload_image():
    form = RegistrationForm(CombinedMultiDict((request.files, request.form)))
    imagefile = photos.save(form.image_file.data)
    imagename = request.form['name']
    # imagefile = request.files.get('image_file')
    flash('file saved')
    newpath='majorproject/newdataset/' + imagename

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    shutil.move(imagefile,newpath+'/'+imagefile)
    return render_template('alert_on_registration.html')

@app.route('/train')
def training():
    start_encoding()
    return render_template('alert_on_training.html')

@app.route('/test')
def upload_testing():
    return render_template('testpage.html')

@app.route('/recognize', methods=['POST'])
def recognize_image():
    imagefile = request.files.get('imagefile', '')       
    filename = secure_filename(imagefile.filename)
    newpath='majorproject/examples/'
    imagefile.save(os.path.join(newpath, filename))         
    name=testing_func('majorproject/examples/'+filename)
    print(name)
    return render_template('result_of_recognition.html',  name=name)