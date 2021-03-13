from flask_restful import Resource
from flask import make_response,request,json
from flask_restful_swagger import swagger
from validate_token import token_required

@swagger.model
class Authenticate(Resource):
    @swagger.operation(
        description="token authentication",
        nickname="token authentication",
        parameters=[
            {
                "name": "X_ACCESS_TOKEN",
                "dataType": "String",
                "description": "Access Token for API request authentication and validation",
                "required": True,
                "allowMultiple": False,
                "paramType": "header"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Token Authenticate succesfully"},
            {"code": 400, "message": "Bad Request: Error on authenticating token"}
        ],
    )
    @token_required
    def get(self):
        try:
            return make_response("token validates successfully")
        except Exception as e:
            print(e)
