import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime


def get_all_medida():
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM T_VB_MEDIDA ORDER BY 1 ASC")
                medidas = cursor.fetchall()

                if len(medidas) == 0:
                    return jsonify({"message": "Nenhuma medida encontrada!"}), 404

                medidas_json = []
                for medida in medidas:
                    medida_dict = {
                        "id": medida[0],
                        "cintura": medida[1],
                        "torax": medida[2],
                        "braco_direito": medida[3],
                        "braco_esquerdo": medida[4],
                        "coxa_direita": medida[5],
                        "coxa_esquerda": medida[6],
                        "panturrilha_direita": medida[7],
                        "panturrilha_esquerda": medida[8],
                        "altura": medida[9],
                        "peso": medida[10],
                        "dt_cadastro": medida[11].strftime('%Y-%m-%d %H:%M:%S'),
                        "nm_usuario": medida[12]
                    }
                    medidas_json.append(medida_dict)
                return jsonify(medidas_json), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500
    

def get_medida_by_id(id):
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(f"SELECT * FROM T_VB_MEDIDA WHERE ID_MEDIDA = {id}")
                medida = cursor.fetchone()

                if medida is None:
                    return jsonify({"message": "Medida não encontrada!"}), 404
                
                medida_dict = {
                    "id": medida[0],
                    "cintura": medida[1],
                    "torax": medida[2],
                    "braco_direito": medida[3],
                    "braco_esquerdo": medida[4],
                    "coxa_direita": medida[5],
                    "coxa_esquerda": medida[6],
                    "panturrilha_direita": medida[7],
                    "panturrilha_esquerda": medida[8],
                    "altura": medida[9],
                    "peso": medida[10],
                    "dt_cadastro": medida[11].strftime('%Y-%m-%d %H:%M:%S'),
                    "nm_usuario": medida[12]
                }
                return jsonify(medida_dict), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500


def criar_medida(data):
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    f"""INSERT INTO T_VB_MEDIDA (ID_MEDIDA, CINTURA_MEDIDA, TORAX_MEDIDA, BRACO_DIREITO_MEDIDA, BRACO_ESQUERDO_MEDIDA, COXA_DIREITA_MEDIDA, COXA_ESQUERDA_MEDIDA, PANTURRILHA_DIREITA_MEDIDA, PANTURRILHA_ESQUERDA_MEDIDA, ALTURA_MEDIDA, PESO_MEDIDA, DT_CADASTRO, NM_USUARIO) 
                    VALUES (SQ_VB_MEDIDA.nextval, {data['cintura']}, {data['torax']}, {data['braco_direito']}, {data['braco_esquerdo']}, {data['coxa_direita']}, {data['coxa_esquerda']}, {data['panturrilha_direita']}, {data['panturrilha_esquerda']}, {data['altura']}, {data['peso']}, SYSDATE, USER)"""
                )
                conn.commit()
                
                cursor.execute("SELECT SQ_VB_MEDIDA.currval FROM DUAL")
                id_medida = cursor.fetchone()[0]
                
                cursor.execute(f"SELECT * FROM T_VB_MEDIDA WHERE ID_MEDIDA = {id_medida}")
                medida = cursor.fetchone()

                medida_dict = {
                    "id": medida[0],
                    "cintura": medida[1],
                    "torax": medida[2],
                    "braco_direito": medida[3],
                    "braco_esquerdo": medida[4],
                    "coxa_direita": medida[5],
                    "coxa_esquerda": medida[6],
                    "panturrilha_direita": medida[7],
                    "panturrilha_esquerda": medida[8],
                    "altura": medida[9],
                    "peso": medida[10],
                    "dt_cadastro": medida[11].strftime('%Y-%m-%d %H:%M:%S'),
                    "nm_usuario": medida[12]
                }
                return jsonify({ "message": "Medida criada com sucesso!", "medida": medida_dict }), 201
            except Exception as e:
                return jsonify({"message": str(e)}), 500


def atualizar_medida(id, data):
    with oracledb.connect(user="rm551451", password="fiap23", dsn="oracle.fiap.com.br/orcl") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    f"""UPDATE T_VB_MEDIDA SET 
                    CINTURA_MEDIDA = {data['cintura']}, 
                    TORAX_MEDIDA = {data['torax']}, 
                    BRACO_DIREITO_MEDIDA = {data['braco_direito']}, 
                    BRACO_ESQUERDO_MEDIDA = {data['braco_esquerdo']}, 
                    COXA_DIREITA_MEDIDA = {data['coxa_direita']}, 
                    COXA_ESQUERDA_MEDIDA = {data['coxa_esquerda']}, 
                    PANTURRILHA_DIREITA_MEDIDA = {data['panturrilha_direita']}, 
                    PANTURRILHA_ESQUERDA_MEDIDA = {data['panturrilha_esquerda']}, 
                    ALTURA_MEDIDA = {data['altura']}, 
                    PESO_MEDIDA = {data['peso']}, 
                    DT_CADASTRO = SYSDATE, 
                    NM_USUARIO = USER
                    WHERE ID_MEDIDA = {id}"""
                )
                conn.commit()

                cursor.execute(f"SELECT * FROM T_VB_MEDIDA WHERE ID_MEDIDA = {id}")
                medida = cursor.fetchone()

                medida_dict = {
                    "id": medida[0],
                    "cintura": medida[1],
                    "torax": medida[2],
                    "braco_direito": medida[3],
                    "braco_esquerdo": medida[4],
                    "coxa_direita": medida[5],
                    "coxa_esquerda": medida[6],
                    "panturrilha_direita": medida[7],
                    "panturrilha_esquerda": medida[8],
                    "altura": medida[9],
                    "peso": medida[10],
                    "dt_cadastro": medida[11].strftime('%Y-%m-%d %H:%M:%S'),
                    "nm_usuario": medida[12]
                }
                return jsonify({ "message": "Medida atualizada com sucesso", "medida": medida_dict }), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500


