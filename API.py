from flask import Flask, jsonify, request
from datetime import datetime
import clientes
import objetivos
import medidas
import biotipos
import dietas
import treinos
import tipo_treinos
import exercicios

app = Flask(__name__)


# CLIENTE  CLIENTE   CLIENTE   CLIENTE   CLIENTE
@app.route("/api/cliente", methods=["GET"])
def get_all_clientes():
    response = clientes.get_all_cliente()
    return response

@app.route("/api/cliente/<int:id>", methods=["GET"])
def get_cliente_by_id(id):
    response = clientes.get_cliente_by_id(id)
    return response

@app.route("/api/cliente/<string:email>", methods=["GET"])
def get_cliente_by_email(email):
    response = clientes.get_cliente_by_email(email)
    return response

@app.route("/api/cliente/login", methods=["POST"])
def login_cliente():
    data = request.get_json()
    response = clientes.login_cliente(data)
    return response

@app.route("/api/cliente", methods=["POST"])
def criar_cliente():
    data = request.get_json()
    response = clientes.criar_cliente(data)
    return response

@app.route("/api/cliente/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    data = request.get_json()
    response = clientes.atualizar_cliente(id, data)
    return response

@app.route("/api/cliente/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    response = clientes.deletar_cliente(id)
    return response



# OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO
@app.route("/api/objetivo", methods=["GET"])
def get_all_objetivo():
    response = objetivos.get_all_objetivo()
    return response

@app.route("/api/objetivo/<int:id>", methods=["GET"])
def get_objetivo_by_id(id):
    response = objetivos.get_objetivo_by_id(id)
    return response

@app.route("/api/objetivo", methods=["POST"])
def criar_objetivo():
    data = request.get_json()
    response = objetivos.criar_objetivo(data)
    return response
    
@app.route("/api/objetivo/<int:id>", methods=["PUT"])
def atualizar_objetivo(id):
    data = request.get_json()
    response = objetivos.atualizar_objetivo(id, data)
    return response



# MEDIDA   MEDIDA   MEDIDA   MEDIDA   MEDIDA
@app.route("/api/medida", methods=["GET"])
def get_all_medida():
    response = medidas.get_all_medida()
    return response

@app.route("/api/medida/<int:id>", methods=["GET"])
def get_medida_by_id(id):
    response = medidas.get_medida_by_id(id)
    return response

@app.route("/api/medida", methods=["POST"])
def criar_medida():
    data = request.get_json()
    response = medidas.criar_medida(data)
    return response

@app.route("/api/medida/<int:id>", methods=["PUT"])
def atualizar_medida(id):
    data = request.get_json()
    response = medidas.atualizar_medida(id, data)
    return response



# BIOTIPO   BIOTIPO   BIOTIPO   BIOTIPO   BIOTIPO
@app.route("/api/biotipo", methods=["GET"])
def get_all_biotipo():
    response = biotipos.get_all_biotipo()
    return response

@app.route("/api/biotipo/<int:id>", methods=["GET"])
def get_biotipo_by_id(id):
    response = biotipos.get_biotipo_by_id(id)
    return response



# DIETA   DIETA   DIETA   DIETA   DIETA
@app.route("/api/dieta", methods=["GET"])
def get_all_dieta():
    response = dietas.get_all_dieta()
    return response
    
@app.route("/api/dieta/<int:id>", methods=["GET"])
def get_dieta_by_id(id):
    response = dietas.get_dieta_by_id(id)
    return response



# TREINO   TREINO   TREINO   TREINO   TREINO
@app.route("/api/treino", methods=["GET"])
def get_all_treino():
    response = treinos.get_all_treino()
    return response

@app.route("/api/treino/<int:id>", methods=["GET"])
def get_treino_by_id(id):
    response = treinos.get_treino_by_id(id)
    return response



# TIPO TREINO   TIPO TREINO   TIPO TREINO   TIPO TREINO   TIPO TREINO
@app.route("/api/tipo-treino", methods=["GET"])
def get_all_tipo_treino():
    response = tipo_treinos.get_all_tipo_treino()
    return response

@app.route("/api/tipo-treino/<int:id>", methods=["GET"])
def get_tipo_treino_by_id(id):
    respose = tipo_treinos.get_tipo_treino_by_id(id)
    return respose

@app.route("/api/tipo-treino/treino/<int:id>", methods=["GET"])
def get_tipo_treino_by_treino(id):
    response = tipo_treinos.get_tipo_treino_by_treino(id)
    return response



# EXERCICIOS  EXERCICIOS   EXERCICIOS   EXERCICIOS   EXERCICIOS
@app.route("/api/exercicio", methods=["GET"])
def get_all_exercicio():
    respose = exercicios.get_all_exercicio()
    return respose

@app.route("/api/exercicio/<int:id>", methods=["GET"])
def get_exercicio_by_id(id):
    response = exercicios.get_exercicio_by_id(id)
    return response

@app.route("/api/exercicio/tipo-treino/<int:id>", methods=["GET"])
def get_exercicio_by_tipo_treino(id):
    response = exercicios.get_exercicio_by_tipo_treino(id)
    return response




app.run(debug=True)