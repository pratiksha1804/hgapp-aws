import os
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = "IAM_AUTHENTICATION"
app.config['MONGO_URI'] = "mongodb://localhost:27017/IAM_AUTHENTICATION"
mongo = PyMongo(app)