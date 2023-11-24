import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime


def get_all_dieta():
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM T_VB_DIETA ORDER BY 1 ASC")
                dietas = cursor.fetchall()

                if len(dietas) == 0:
                    return jsonify({"message": "Nenhuma dieta encontrada!"}), 404

                dietas_json = []
                for dieta in dietas:
                    dieta_dict = {
                        "id": dieta[0],
                        "nome": dieta[1],
                        "descricao": json.loads(dieta[2].read()) if dieta[2] else None,
                    }
                    dietas_json.append(dieta_dict)
                return jsonify(dietas_json)
            except Exception as e:
                return jsonify({"message": str(e)}), 500
    

def get_dieta_by_id(id):
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(f"SELECT * FROM T_VB_DIETA WHERE ID_DIETA = {id}")
                dieta = cursor.fetchone()

                if dieta is None:
                    return jsonify({"message": "Dieta não encontrada!"}), 404
                
                dieta_dict = {
                    "id": dieta[0],
                    "nome": dieta[1],
                    "descricao": json.loads(dieta[2].read()) if dieta[2] else None,
                }
                return jsonify(dieta_dict), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500

