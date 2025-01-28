from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/somar', methods=['POST'])
def somar():
    """
    Recebe dois números via POST (JSON) e retorna a soma.
    """
    dados = request.get_json()
    num1 = dados.get('num1')
    num2 = dados.get('num2')

    # Validação simples
    if num1 is None or num2 is None:
        return jsonify({"erro": "Os campos 'num1' e 'num2' são obrigatórios."}), 400

    try:
        resultado = float(num1) + float(num2)
        return jsonify({"resultado": resultado}), 200
    except ValueError:
        return jsonify({"erro": "Os valores devem ser números válidos."}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5001)
