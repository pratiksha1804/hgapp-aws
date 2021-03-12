from flask_restful import Resource
from flask import make_response, request, jsonify
from flask_restful_swagger import swagger
import jwt, json
import datetime
import database
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
            payload = json.loads(request.data)
            username = payload["username"]
            password = payload["password"]

            # data = database.validateUser(username, password)
            # if data:
            if username == "pratiksha" and password == "pratiksha":
                token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
                return make_response(token)

            return make_response('could not verify!', 401)


        except Exception as e:
            print(e)
