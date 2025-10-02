from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(name)
CORS(app)  # Permite requisições de qualquer origem

votos = {"Opção A": 0, "Opção B": 0}

@app.route("/vote", methods=["POST"])
def votar():
    data = request.json
    opcao = data.get("opcao")
    if opcao in votos:
        votos[opcao] += 1
        return jsonify({"mensagem": "Voto computado com sucesso!"}), 200
    return jsonify({"erro": "Opção inválida"}), 400

@app.route("/results", methods=["GET"])
def resultados():
    return jsonify(votos), 200

if name == "main":
    app.run(host="0.0.0.0", port=5001)