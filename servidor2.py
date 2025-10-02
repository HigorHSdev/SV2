from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Inicializa o app Flask
app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios

# Rota de teste
@app.route("/")
def home():
    return jsonify({"message": "Servidor 2 rodando!"})

# Exemplo de rota POST
@app.route("/dados", methods=["POST"])
def receber_dados():
    data = request.get_json()
    return jsonify({"dados_recebidos": data, "status": "sucesso"})

# Inicia o servidor
if __name__ == "__main__":
    # Usa porta do Render, ou 5000 como fallback
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
