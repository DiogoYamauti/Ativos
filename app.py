from flask import Flask, request, jsonify
from db import get_db

app = Flask(__name__)
db = get_db()
funcionarios_collection = db['funcionarios']

# Limites máximos para cada ativo conforme especificado na planilha
MAX_ATIVOS = {
    "notebook": 1,
    "monitor1": 1,
    "monitor2": 1,
    "teclado": 1,
    "mouse": 1,
    "nobreak": 1,
    "desktop": 1,
    "headset": 1,
    "celular": 1,
    "acessorios": 1
}

def order_funcionario_data(funcionario):
    order = ["cpf", "nome", "notebook", "monitor1", "monitor2", "teclado", "mouse", "desktop", "acessorios", "nobreak", "headset", "celular"]
    return {key: funcionario.get(key) for key in order if key in funcionario}

@app.route('/funcionarios', methods=['POST'])
def adicionar_funcionario():
    data = request.json
    if funcionarios_collection.find_one({"cpf": data['cpf']}):
        return jsonify({"error": "Funcionário com esse CPF já existe"}), 400
    try:
        funcionarios_collection.insert_one(data)
        return jsonify({"message": "Funcionário adicionado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = list(funcionarios_collection.find({}, {"_id": 0}))
    ordered_funcionarios = [order_funcionario_data(funcionario) for funcionario in funcionarios]
    return jsonify(ordered_funcionarios), 200

@app.route('/funcionarios/<cpf>', methods=['GET'])
def consultar_funcionario(cpf):
    funcionario = funcionarios_collection.find_one({"cpf": cpf}, {"_id": 0})
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404
    return jsonify(order_funcionario_data(funcionario)), 200

@app.route('/funcionarios/<cpf>', methods=['PUT'])
def atualizar_funcionario(cpf):
    data = request.json
    result = funcionarios_collection.update_one({"cpf": cpf}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"error": "Funcionário não encontrado"}), 404
    return jsonify({"message": "Funcionário atualizado com sucesso"}), 200

@app.route('/funcionarios/<cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    funcionario = funcionarios_collection.find_one({"cpf": cpf})
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404
    # Verificar se há ativos atribuídos
    for ativo, valor in MAX_ATIVOS.items():
        if ativo in funcionario and funcionario[ativo]:
            return jsonify({"error": "Funcionário possui ativos atribuídos"}), 400
    funcionarios_collection.delete_one({"cpf": cpf})
    return jsonify({"message": "Funcionário excluído com sucesso"}), 200

@app.route('/funcionarios/<cpf>/ativos', methods=['PUT'])
def atualizar_ativos(cpf):
    data = request.json
    funcionario = funcionarios_collection.find_one({"cpf": cpf})
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404

    # Verificar regras de negócio
    for key, value in data.items():
        if key not in MAX_ATIVOS:
            return jsonify({"error": f"Ativo {key} não permitido"}), 400
        if key in funcionario and funcionario[key]:
            return jsonify({"error": f"Funcionário já possui {key}"}), 400

    result = funcionarios_collection.update_one({"cpf": cpf}, {"$set": data})
    return jsonify({"message": "Ativos atualizados com sucesso"}), 200

@app.route('/funcionarios/<cpf>/ativos', methods=['DELETE'])
def limpar_ativos(cpf):
    data = request.json
    funcionario = funcionarios_collection.find_one({"cpf": cpf})
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404

    # Limpar ativos especificados
    update_data = {}
    for key in data.keys():
        if key not in MAX_ATIVOS:
            return jsonify({"error": f"Ativo {key} não permitido"}), 400
        if key in funcionario and funcionario[key]:
            update_data[key] = None

    result = funcionarios_collection.update_one({"cpf": cpf}, {"$set": update_data})
    return jsonify({"message": "Ativos limpos com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
