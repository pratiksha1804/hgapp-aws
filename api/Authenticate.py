from flask_restful import Resource
from flask import make_response,request,json
from flask_restful_swagger import swagger

@swagger.model
class Authenticate(Resource):
    @swagger.operation(
        description="user authentication",
        nickname="user authentication",
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
            {"code": 200, "message": "User Authenticate succesfully"},
            {"code": 400, "message": "Bad Request: Error on authenticating user"}
        ],
    )
    def post(self):
        try:
            pass

        except Exception as e:
            print(e)
