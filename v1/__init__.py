from os import environ
from flask import Flask
from flask_jwt_extended import  JWTManager
from flask_cors import CORS

from config import app_config

'''creating the app'''
env = environ.get("APP_SETTINGS")
app = Flask(__name__)
app.config['JWT_SECRET_KEY']= 'secret'
app.config.from_object(app_config[env])
print(app_config[env])
jwt = JWTManager(app)
CORS(app)


''' importing routes '''
from v1 import views