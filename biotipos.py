import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")


def get_all_biotipo():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_VB_BIOTIPO ORDER BY 1 ASC")
        biotipos = cursor.fetchall()

        if len(biotipos) == 0:
            return jsonify({"message": "Nenhum biotipo encontrado!"}), 404

        biotipos_json = []
        for biotipo in biotipos:
            biotipo_dict = {
                "id": biotipo[0],
                "nome": biotipo[1],
                "descricao": biotipo[2],
            }
            biotipos_json.append(biotipo_dict)

        return jsonify(biotipos_json), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def get_biotipo_by_id(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_BIOTIPO WHERE ID_BIOTIPO = {id}")
        biotipo = cursor.fetchone()

        if biotipo is None:
            return jsonify({"message": "Biotipo não encontrado!"}), 404
        
        biotipo_dict = {
            "id": biotipo[0],
            "nome": biotipo[1],
            "descricao": biotipo[2],
        }

        return jsonify(biotipo_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
