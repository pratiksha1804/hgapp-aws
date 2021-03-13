import os
from config import app
from api import api
from api.Login import Login
from api.Authenticate import Authenticate
from flask import request,jsonify

api.add_resource(Login, '/api/login')
api.add_resource(Authenticate, '/api/authenticate')

import jwt
app.config['SECRET_KEY'] = 'thisisthesecretkey'
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing!'}),403
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Token is invalid'}),403

        return f(*args,**kwargs)
    return decorated

@app.route('/protected')
@token_required
def protected():
     return jsonify({"message":"this aws is protected site"})


if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5002, debug=True)