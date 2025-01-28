from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para evitar problemas de acesso externo

@app.route('/api/somar', methods=['POST'])
def somar():
    dados = request.get_json()
    num1 = dados.get('num1')
    num2 = dados.get('num2')

    if num1 is None or num2 is None:
        return jsonify({"erro": "Os campos 'num1' e 'num2' são obrigatórios."}), 400

    try:
        resultado = float(num1) + float(num2)
        return jsonify({"resultado": resultado}), 200
    except ValueError:
        return jsonify({"erro": "Os valores devem ser números válidos."}), 400

if __name__ == '__main__':
    app.run(debug=True)
