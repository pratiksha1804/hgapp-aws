import jwt
from config import app
from flask import jsonify, request
from flask import jsonify, request,make_response

app.config['SECRET_KEY'] = 'thisisthesecretkey'
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # token= request.headers['X_ACCESS_TOKEN']
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJleHAiOjE2MTU2MTgyMzV9.WKzfVB6rMJk8UQXKWB_M1R-5zI41-mQg-GouSrrpPhc'
        if not token:
            return jsonify({'message':'Token is missing!'}),403
        try:
            data =jwt.decode(token,app.config['SECRET_KEY'],algorithms="HS256")
        except:
            return make_response('Token is invalid')

        return f(*args,**kwargs)
    return decorated