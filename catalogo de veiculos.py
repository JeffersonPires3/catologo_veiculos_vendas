from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['catalogo_veiculos']
collection = db['veiculos']

@app.route('/veiculos', methods=['GET'])
def get_veiculos():
    veiculos = list(collection.find())
    return jsonify(veiculos)

@app.route('/veiculos', methods=['POST'])
def add_veiculo():
    veiculo = request.json
    veiculo_id = collection.insert_one(veiculo).inserted_id
    return jsonify(str(veiculo_id))

@app.route('/veiculos/<veiculo_id>', methods=['PUT'])
def update_veiculo(veiculo_id):
    veiculo = request.json
    result = collection.update_one({'_id': veiculo_id}, {'$set': veiculo})
    return jsonify(str(result.modified_count))

@app.route('/veiculos/<veiculo_id>', methods=['DELETE'])
def delete_veiculo(veiculo_id):
    result = collection.delete_one({'_id': veiculo_id})
    return jsonify(str(result.deleted_count))

if __name__ == '__main__':
    app.run()
