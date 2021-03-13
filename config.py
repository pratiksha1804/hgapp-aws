import os
from flask import Flask
from flask_pymongo import PyMongo
import constants

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "IAM_AUTHENTICATION"
app.config['MONGO_URI'] = "mongodb://"+constants.MONGO_USERNAME+":"+constants.MONGO_PASSWORD+"@"+constants.MONGO_URL+":"+constants.MONGO_PORT+"?authSource=admin"
mongo = PyMongo(app)