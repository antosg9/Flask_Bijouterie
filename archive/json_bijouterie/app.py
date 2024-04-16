from flask import Flask,request, jsonify
import json

app = Flask(__name__)
stone="pierres.json"

@app.route("/", methods=['GET'])
def get():
    with open(stone, 'r') as json_file:
        data=json.load(json_file)
    return jsonify(data)

@app.route("/", methods=['POST'])
def post():
    json_data=request.get_json()
    
    with open(stone, 'r+') as file:
        data=json.load(file)
        if type(json_data)==list:
            for element in json_data:
                data.append(element)
        elif type(json_data)==dict:
            data.append(json_data)
        else:
            return jsonify({'Error': 'Le format de donnée est invalide'}), 400
        file.seek(0)
        json.dump(data,file,indent=4)
        
    return jsonify({'Message' : 'Donnees ajoutees avec succes'}), 200

    