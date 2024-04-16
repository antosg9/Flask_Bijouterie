from flask import Flask,request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://<userName>:<password>@singlebox.1uclju8.mongodb.net/?retryWrites=true&w=majority&appName=SingleBox" #Remplacer <userName> et <password> par les logs à la base de données MangoDB
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.Bijouterie
collection=db.Pierres

@app.route('/', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)

@app.route("/", methods=['POST'])
def post():
    json_data=request.get_json()
    
    if type(json_data)==list:
        result=collection.insert_many(json_data)
        id=result.inserted_ids
    
    elif type(json_data)==dict:
        result=collection.insert_one(json_data)
        id=[result.inserted_id]
    else:
        return jsonify({"Erreur : Le format de donnée est invalide !"}), 400
    
    if id:
        return jsonify({'Message' : 'Donnees ajoutees avec succes'}), 200
    else:
        return jsonify({"Erreur lors de l'insertion des données."}), 500
