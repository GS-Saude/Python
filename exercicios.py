import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")



def get_all_exercicio():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_VB_EXERC ORDER BY 1 ASC")
        exercicios = cursor.fetchall()

        if len(exercicios) == 0:
            return jsonify({"message": "Nenhum exercicio encontrado!"}), 404
        
        exercicios_json = []
        for exercicio in exercicios:
            exercicio_dict = {
                "id": exercicio[0],
                "nome": exercicio[1],
                "descricao": exercicio[2],
            }
            exercicios_json.append(exercicio_dict)

        return jsonify(exercicios_json), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def get_exercicio_by_id(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_EXERC WHERE ID_EXERCICIO = {id}")
        exercicio = cursor.fetchone()

        if exercicio is None:
            return jsonify({"message": "Exercicio não encontrado!"}), 404
        
        exercicio_dict = {
            "id": exercicio[0],
            "nome": exercicio[1],
            "descricao": exercicio[2],
        }

        return jsonify(exercicio_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_exercicio_by_tipo_treino(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT E.ID_EXERCICIO, E.NM_EXERCICIO, E.SERIES_EXERCICIO, E.REPETICOES_EXERCICIO, E.TEMPO_DESCANSO_EXERCICIO
            FROM T_VB_EXERC E
            INNER JOIN T_VB_TP_TREINO TP ON TP.ID_TP_TREINO = E.ID_TP_TREINO
            WHERE TP.ID_TP_TREINO = {id}
            ORDER BY 1 ASC
        """)
        exercicios = cursor.fetchall()

        if len(exercicios) == 0:
            return jsonify({"message": "Nenhum exercicio encontrado!"}), 404
        
        exercicios_json = []
        for exercicio in exercicios:
            exercicio_dict = {
                "id": exercicio[0],
                "nome": exercicio[1],
                "series": exercicio[2],
                "repeticoes": exercicio[3],
                "tempo_descanso": exercicio[4],
            }
            exercicios_json.append(exercicio_dict)
        
        return jsonify(exercicios_json), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500










