import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")



def get_all_treino():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_VB_TREINO ORDER BY 1 ASC")
        treinos = cursor.fetchall()

        if len(treinos) == 0:
            return jsonify({"message": "Nenhum treino encontrado!"}), 404

        treinos_json = []
        for treino in treinos:
            treino_dict = {
                "id": treino[0],
                "nome": treino[1],
                "descricao": treino[2],
            }
            treinos_json.append(treino_dict)

        return jsonify(treinos_json), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_treino_by_id(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_TREINO WHERE ID_TREINO = {id}")
        treino = cursor.fetchone()

        if treino is None:
            return jsonify({"message": "Treino não encontrado!"}), 404
        
        treino_dict = {
            "id": treino[0],
            "nome": treino[1],
            "descricao": treino[2],
        }

        return jsonify(treino_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

