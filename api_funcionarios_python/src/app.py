from flask import Flask, request, jsonify
from funcionario import Funcionario
from funcionarios import Funcionarios
import json

app = Flask(__name__)


@app.route("/funcionarios", methods=["GET"])
def get_funcionarios():
    funcionarios = Funcionarios()
    funcionou, lista = funcionarios.select_funcionarios()
    if funcionou:
        response = jsonify({"funcionarios": lista})
        return response, 200
    return "NOT FOUND", 404


@app.route("/funcionarios", methods=["POST"])
def add_funcionario():
    request_data = request.get_json()
    funcionario_data = request_data["funcionario"]

    funcionario = Funcionario(
        funcionario_data["cargo"],
        funcionario_data["id_setor"],
        funcionario_data["qtd_dependentes"],
        funcionario_data["nome"],
        funcionario_data["sexo"],
        funcionario_data["data_nascimento"],
        funcionario_data["salario"],
    )

    funcionario.insert_funcionario()

    return "OK", 201


@app.route("/funcionarios/<int:id>", methods=["GET"])
def get_funcionario_by_id(id):
    funcionarios = Funcionarios()
    funcionou, lista = funcionarios.select_funcionarios()
    if funcionou:
        for funcionario in lista:
            if funcionario['id'] == id:
                return funcionario, 200
    return "ERROR", 404


@app.route("/funcionarios/<id>", methods=["PUT"])
def update_funcionario(id):
    request_data = request.get_json()
    funcionario_data = request_data["funcionario"]
                
    funcionario = Funcionario(None, 0, 0, None, None, None, 0)
    funcionario.select_funcionario(id)
    funcionario.cargo = funcionario_data["cargo"]
    funcionario.salario = funcionario_data["salario"]
    funcionario.id_setor = funcionario_data["id_setor"]
    if funcionario.update_funcionario():
        return "OK", 200
    return "NOT FOUND", 404


@app.route("/funcionarios/<id>", methods=["DELETE"])
def delete_funcionario(id):
    funcionario = Funcionario(None, 0, 0, None, None, None, 0)
    funcionario.select_funcionario(id)
    if funcionario.delete_funcionario():
        return "OK", 204
    return "NOT FOUND", 404
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
