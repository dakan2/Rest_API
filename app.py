#import library
from urllib import response
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask (__name__)

# inisiasi object flask_restful
api = Api (app)

# Inisiasi object flask cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary
identitas = {} #variable global, dictionary = json

#membuat class Resource
class ContohResource(Resource) : 
    # metode get dan post 
    def get(self) : 
       # response = {"msg" :"Halo Dunia, ini apa restfull pertamakku"}
        return identitas 

    def post(self) : 
        nama = request.form["nama"] 
        umur = request.form["umur"]
        identitas["nama"]=nama
        identitas["umur"]=umur

# setup resource
api.add_resource(ContohResource,"/api",methods =["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)