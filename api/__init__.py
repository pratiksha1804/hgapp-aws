from flask_restful import Api
from flask_restful_swagger import swagger
from config import app

api = swagger.docs(
Api(app),
basePath="http://0.0.0.0:5002",
resourcePath="/",
produces=["application/json", "text/html"],
api_spec_url="/api/spec",
description="authentication service",
)

