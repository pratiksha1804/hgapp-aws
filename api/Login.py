from flask_restful import Resource
from flask import make_response, request, jsonify
from flask_restful_swagger import swagger
import jwt, json
import datetime
import database
import base64
from config import app
app.config['SECRET_KEY'] = 'thisisthesecretkey'

@swagger.model
class Login(Resource):
    @swagger.operation(
        description="user login",
        nickname="user login",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "User Logged in succesfully"},
            {"code": 400, "message": "Bad Request: Error on logging in user"}
        ],
    )
    def post(self):
        try:
            payload = json.loads(request.data.decode())
            username = payload["username"]
            password = payload["password"]

            data = database.validateUser(username)
            if data:
                print("data role..", data['roleid'])
                if data['password'] == password:
                    role = database.getRole(data['roleid'])
                    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30), 'role':role['role']},app.config['SECRET_KEY'])
                    # return jsonify({'token':jwt.decode(token,app.config['SECRET_KEY'],algorithms="HS256")})
                    return jsonify({'token':token})


            return make_response('could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required" '})


        except Exception as e:
            return  make_response('error: ',e)
