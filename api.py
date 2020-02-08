from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
api = Api(app)

client = MongoClient()

print(client)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
