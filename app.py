import os
from config import app
from api import api
from api.Login import Login
from api.Authenticate import Authenticate

api.add_resource(Login, '/api/login')
api.add_resource(Authenticate, '/api/authenticate')

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5002, debug=True)