from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

ARQUIVO_VOTOS = "votos.json"

#Função para ler votos
def ler_votos():
    if not os.path.exists(ARQUIVO_VOTOS):
        return {"votos": []}
    with open(ARQUIVO_VOTOS, "r") as file:
        return json.load(file)

#Função para salvar votos
def salvar_votos(dados):
    with open(ARQUIVO_VOTOS, "w") as file:
        json.dump(dados, file, indent=4)

@app.route("/")
def home():
    return jsonify({"message": "Servidor 2 rodando!"})

#Rota para receber votos
@app.route("/vote", methods=["POST"])
def votar():
    data = request.get_json()
    nome = data.get("nome")
    opcao = data.get("opcao")

    if not nome or not opcao:
        return jsonify({"status": "erro", "mensagem": "Nome e opção são obrigatórios"}), 400

    votos_atuais = ler_votos()
    votos_atuais["votos"].append({"nome": nome, "opcao": opcao})
    salvar_votos(votos_atuais)

    return jsonify({"status": "sucesso", "mensagem": "Voto registrado"})

#Rota para mostrar resultados (apenas total)
@app.route("/results", methods=["GET"])
def resultados():
    votos = ler_votos()
    total = len(votos["votos"])
    return jsonify({"total": total})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)