import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")



def get_all_objetivo():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_VB_OBJETIVO ORDER BY 1 ASC")
        objetivos = cursor.fetchall()

        if len(objetivos) == 0:
            return jsonify({"message": "Nenhum objetivo encontrado!"}), 404

        objetivos_json = []
        for objetivo in objetivos:
            objetivo_dict = {
                "id": objetivo[0],
                "nome": objetivo[1],
                "tempo": objetivo[2].strftime('%d/%m/%Y'),
                "peso": objetivo[3],
            }
            objetivos_json.append(objetivo_dict)

        return jsonify(objetivos_json), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def get_objetivo_by_id(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_OBJETIVO WHERE ID_OBJETIVO = {id}")
        objetivo = cursor.fetchone()

        if objetivo is None:
            return jsonify({"message": "Objetivo não encontrado!"}), 404
        
        objetivo_dict = {
            "id": objetivo[0],
            "nome": objetivo[1],
            "tempo": objetivo[2].strftime('%d/%m/%Y'),
            "peso": objetivo[3],
        }

        return jsonify(objetivo_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def criar_objetivo(data):
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""INSERT INTO T_VB_OBJETIVO (ID_OBJETIVO, NM_OBJETIVO, PESO_OBJETIVO, TEMPO_OBJETIVO, DT_CADASTRO, NM_USUARIO) 
            VALUES (SQ_VB_OBJETIVO.nextval, '{data['nome']}', {data['peso']}, TO_DATE('{data['tempo']}', 'DD/MM/YYYY'), SYSDATE, USER)"""
        )
        conn.commit()

        cursor.execute("SELECT SQ_VB_OBJETIVO.currval FROM DUAL")
        id = cursor.fetchone()[0]

        cursor.execute(f"SELECT * FROM T_VB_OBJETIVO WHERE ID_OBJETIVO = {id}")
        objetivo = cursor.fetchone()
        
        objetivo_dict = {
            "id": objetivo[0],
            "nome": objetivo[1],
            "peso": objetivo[2],
            "tempo": objetivo[3],
        }

        return jsonify({ "message": "Objetivo criado com sucesso!", "objetivo": objetivo_dict }), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def atualizar_objetivo(id, data):
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""UPDATE T_VB_OBJETIVO SET 
            NM_OBJETIVO = '{data['nome']}', 
            PESO_OBJETIVO = {data['peso']}, 
            TEMPO_OBJETIVO = TO_DATE('{data['tempo']}', 'DD/MM/YYYY'),
            DT_CADASTRO = SYSDATE,
            NM_USUARIO = USER
            WHERE ID_OBJETIVO = {id}"""
        )
        conn.commit()

        cursor.execute(f"SELECT * FROM T_VB_OBJETIVO WHERE ID_OBJETIVO = {id}")
        objetivo = cursor.fetchone()

        return jsonify({ "message": "Objetivo atualizado com sucesso", "objetivo": objetivo }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500