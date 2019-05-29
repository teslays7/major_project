from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# UPLOAD_FOLDER = 'dataset'
basedir='/Users/yashsharma/Major_Project'
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

db =SQLAlchemy(app)

from majorproject import routes