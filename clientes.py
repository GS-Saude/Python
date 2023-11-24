import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")


def get_all_cliente():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_VB_CLIENTE ORDER BY 1 ASC")
        clientes = cursor.fetchall()

        if len(clientes) == 0:
            return jsonify({"message": "Nenhum cliente encontrado!"}), 404

        clientes_json = []
        for cliente in clientes:
            cliente_dict = {
                "id_cliente": cliente[0],
                "id_medida": cliente[1],
                "id_objetivo": cliente[2],
                "id_biotipo": cliente[3],
                "id_dieta": cliente[4],
                "id_treino": cliente[5],
                "email_cliente": cliente[6],
                "senha_cliente": cliente[7],
                "nm_cliente": cliente[8],
                "genero_cliente": cliente[9],
                "idade_cliente": cliente[10],
                "metabolismo_cliente": cliente[11],
            }
            clientes_json.append(cliente_dict)

        return jsonify(clientes_json), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def get_cliente_by_id(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_CLIENTE WHERE ID_CLIENTE = {id}")
        cliente = cursor.fetchone()

        if cliente is None:
            return jsonify({"message": "Cliente não encontrado!"}), 404
        
        cliente_dict = {
            "id_cliente": cliente[0],
            "id_medida": cliente[1],
            "id_objetivo": cliente[2],
            "id_biotipo": cliente[3],
            "id_dieta": cliente[4],
            "id_treino": cliente[5],
            "email_cliente": cliente[6],
            "senha_cliente": cliente[7],
            "nm_cliente": cliente[8],
            "genero_cliente": cliente[9],
            "idade_cliente": cliente[10],
            "metabolismo_cliente": cliente[11],
        }

        return jsonify(cliente_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def get_cliente_by_email(email):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_CLIENTE WHERE EMAIL_CLIENTE = '{email}'")
        cliente = cursor.fetchone()

        if cliente is None:
            return jsonify({"message": "Cliente não encontrado!"}), 404
        
        cliente_dict = {
            "id_cliente": cliente[0],
            "id_medida": cliente[1],
            "id_objetivo": cliente[2],
            "id_biotipo": cliente[3],
            "id_dieta": cliente[4],
            "id_treino": cliente[5],
            "email_cliente": cliente[6],
            "senha_cliente": cliente[7],
            "nm_cliente": cliente[8],
            "genero_cliente": cliente[9],
            "idade_cliente": cliente[10],
            "metabolismo_cliente": cliente[11],
        }
        return jsonify(cliente_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def login_cliente(data):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM T_VB_CLIENTE WHERE EMAIL_CLIENTE = '{data['email_cliente']}' AND SENHA_CLIENTE = '{data['senha_cliente']}'")
        cliente = cursor.fetchone()

        if cliente is None:
            return jsonify({"message": "Cliente não encontrado!"}), 404

        cliente_dict = {
            "id_cliente": cliente[0],
            "id_medida": cliente[1],
            "id_objetivo": cliente[2],
            "id_biotipo": cliente[3],
            "id_dieta": cliente[4],
            "id_treino": cliente[5],
            "email_cliente": cliente[6],
            "senha_cliente": cliente[7],
            "nm_cliente": cliente[8],
            "genero_cliente": cliente[9],
            "idade_cliente": cliente[10],
            "metabolismo_cliente": cliente[11],
        }
        return jsonify(cliente_dict), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def criar_cliente(data):
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO T_VB_CLIENTE (ID_CLIENTE, ID_MEDIDA, ID_OBJETIVO, ID_BIOTIPO, ID_DIETA, ID_TREINO, EMAIL_CLIENTE, SENHA_CLIENTE, NM_CLIENTE, GENERO_CLIENTE, IDADE_CLIENTE, METABOLISMO_CLIENTE, DT_CADASTRO, NM_USUARIO) 
        VALUES (
            SQ_VB_USUARIO.nextval, {data['id_medida']}, {data['id_objetivo']}, {data['id_biotipo']}, 
            {data['id_dieta']}, {data['id_treino']}, '{data['email_cliente']}', '{data['senha_cliente']}', 
            '{data['nm_cliente']}', '{data['genero_cliente']}', {data['idade_cliente']}, {data['metabolismo_cliente']}, 
            SYSDATE, 
            USER)"""
    )
    conn.commit()
    cursor.execute("SELECT SQ_VB_USUARIO.currval FROM DUAL")
    id_cliente = cursor.fetchone()[0]
    cursor.execute(f"SELECT * FROM T_VB_CLIENTE WHERE ID_CLIENTE = {id_cliente}")
    cliente = cursor.fetchone()
    cliente_dict = {
        "id_cliente": cliente[0],
        "id_medida": cliente[1],
        "id_objetivo": cliente[2],
        "id_biotipo": cliente[3],
        "id_dieta": cliente[4],
        "id_treino": cliente[5],
        "email_cliente": cliente[6],
        "senha_cliente": cliente[7],
        "nm_cliente": cliente[8],
        "genero_cliente": cliente[9],
        "idade_cliente": cliente[10],
        "metabolismo_cliente": cliente[11],
    }
    return jsonify({"message": "Cliente criado com sucesso!", "cliente": cliente_dict}), 201


def atualizar_cliente(id, data):
    try:
        data = request.get_json()
        cursor = conn.cursor()

        cursor.execute(
            f"""UPDATE T_VB_CLIENTE SET 
            ID_MEDIDA = {data['id_medida']}, 
            ID_OBJETIVO = {data['id_objetivo']}, 
            ID_BIOTIPO = {data['id_biotipo']}, 
            ID_DIETA = {data['id_dieta']}, 
            ID_TREINO = {data['id_treino']}, 
            EMAIL_CLIENTE = '{data['email_cliente']}', 
            SENHA_CLIENTE = '{data['senha_cliente']}', 
            NM_CLIENTE = '{data['nm_cliente']}', 
            GENERO_CLIENTE = '{data['genero_cliente']}', 
            IDADE_CLIENTE = {data['idade_cliente']}, 
            METABOLISMO_CLIENTE = {data['metabolismo_cliente']},
            DT_CADASTRO = SYSDATE,
            NM_USUARIO = USER
            WHERE ID_CLIENTE = {id}"""
        )
        conn.commit()

        cursor.execute(f"SELECT * FROM T_VB_CLIENTE WHERE ID_CLIENTE = {id}")
        cliente = cursor.fetchone()

        cliente_dict = {
            "id_cliente": cliente[0],
            "id_medida": cliente[1],
            "id_objetivo": cliente[2],
            "id_biotipo": cliente[3],
            "id_dieta": cliente[4],
            "id_treino": cliente[5],
            "email_cliente": cliente[6],
            "senha_cliente": cliente[7],
            "nm_cliente": cliente[8],
            "genero_cliente": cliente[9],
            "idade_cliente": cliente[10],
            "metabolismo_cliente": cliente[11],
        }

        return jsonify({ "message": "Cliente atualizado com sucesso", "cliente": cliente_dict }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def deletar_cliente(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM T_VB_CLIENTE WHERE ID_CLIENTE = {id}")
        conn.commit()

        return jsonify({"message": "Cliente deletado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

















