from flask import Flask,jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

BOOKS=[{
	"id":1,
	"author":"JJ Patil",
	"price":300
},
{
	"id":2,
	"author":"Godan",
	"price":250
},
{
	"id":3,
	"author":"Patanjali",
	"price":100
}]

class Library(Resource):

	def get(self):
		return BOOKS

	def post(self):
		data = request.get_json()
		BOOKS.append(data)
		return data, 201
	
api.add_resource(Library, '/books')


if __name__ == '__main__':
	app.run(debug = True)
