import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime


def get_all_tipo_treino():
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM T_VB_TP_TREINO ORDER BY 1 ASC")
                tipo_treinos = cursor.fetchall()

                if len(tipo_treinos) == 0:
                    return jsonify({"message": "Nenhum tipo de treino encontrado!"}), 404
                
                tipo_treinos_json = []
                for tipo_treino in tipo_treinos:
                    tipo_treino_dict = {
                        "id": tipo_treino[0],
                        "nome": tipo_treino[1],
                        "descricao": tipo_treino[2],
                    }
                    tipo_treinos_json.append(tipo_treino_dict)
                return jsonify(tipo_treinos_json), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500
    

def get_tipo_treino_by_id(id):
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(f"SELECT * FROM T_VB_TP_TREINO WHERE ID_TP_TREINO = {id}")
                tipo_treino = cursor.fetchone()

                if tipo_treino is None:
                    return jsonify({"message": "Tipo de treino não encontrado!"}), 404
                
                tipo_treino_dict = {
                    "id": tipo_treino[0],
                    "nome": tipo_treino[1],
                    "descricao": tipo_treino[2],
                }
                return jsonify(tipo_treino_dict), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500


def get_tipo_treino_by_treino(id):
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(f"""
                    SELECT 
                        TP.ID_TP_TREINO, 
                        TP.NM_TP_TREINO, 
                        TP.DS_TP_TREINO,
                        T.ID_TREINO, 
                        T.NM_TREINO, 
                        T.DS_TREINO
                    FROM T_VB_TP_TREINO TP
                    INNER JOIN T_VB_TREINO T ON T.ID_TREINO = TP.ID_TREINO
                    WHERE TP.ID_TREINO = {id}
                    ORDER BY 1 ASC
                """)
                tipo_treinos = cursor.fetchall()

                if len(tipo_treinos) == 0:
                    return jsonify({"message": "Nenhum tipo de treino encontrado!"}), 404
                
                tipo_treinos_json = []
                for tipo_treino in tipo_treinos:
                    treino_dict = { 
                        "id_tipo_treino": tipo_treino[0],
                        "nome_tipo_treino": tipo_treino[1],
                        "descricao_tipo_treino": tipo_treino[2],
                        "treino": {
                            "id_treino": tipo_treino[3],
                            "nome_treino": tipo_treino[4],
                            "descricao_treino": tipo_treino[5],
                        },
                    }
                    tipo_treinos_json.append(treino_dict)
                return jsonify(tipo_treinos_json), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500


