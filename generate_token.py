import jwt, json
from flask import make_response, request, jsonify
import datetime
from config import app
app.config['SECRET_KEY'] = 'thisisthesecretkey'

def generateToken(username, role):
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30), 'role': role},
        app.config['SECRET_KEY'])
    return token