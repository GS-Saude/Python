import oracledb
from flask import Flask, jsonify, request
import json
from datetime import datetime

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")
app = Flask(__name__)

# CLIENTE  CLIENTE   CLIENTE   CLIENTE   CLIENTE
# CLIENTE  CLIENTE   CLIENTE   CLIENTE   CLIENTE
@app.route("/api/cliente", methods=["GET"])
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

@app.route("/api/cliente/<int:id>", methods=["GET"])
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

@app.route("/api/cliente/<string:email>", methods=["GET"])
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

@app.route("/api/cliente/login", methods=["POST"])
def login_cliente():
    try:
        data = request.get_json()
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

@app.route("/api/cliente", methods=["POST"])
def criar_cliente():
    data = request.get_json()
    cursor = conn.cursor()
    print(data)

    cursor.execute(
        f"""INSERT INTO T_VB_CLIENTE 
        (ID_CLIENTE, 
        ID_MEDIDA, 
        ID_OBJETIVO, 
        ID_BIOTIPO, 
        ID_DIETA, 
        ID_TREINO, 
        EMAIL_CLIENTE, 
        SENHA_CLIENTE, 
        NM_CLIENTE, 
        GENERO_CLIENTE, 
        IDADE_CLIENTE, 
        METABOLISMO_CLIENTE, 
        DT_CADASTRO, 
        NM_USUARIO) 
        VALUES (
            SQ_VB_USUARIO.nextval, 
            {data['id_medida']}, 
            {data['id_objetivo']}, 
            {data['id_biotipo']}, 
            {data['id_dieta']}, 
            {data['id_treino']}, 
            '{data['email_cliente']}', 
            '{data['senha_cliente']}', 
            '{data['nm_cliente']}', 
            '{data['genero_cliente']}', 
            {data['idade_cliente']}, 
            {data['metabolismo_cliente']}, 
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

@app.route("/api/cliente/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
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


@app.route("/api/cliente/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM T_VB_CLIENTE WHERE ID_CLIENTE = {id}")
        conn.commit()

        return jsonify({"message": "Cliente deletado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO
# OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO
@app.route("/api/objetivo", methods=["GET"])
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

@app.route("/api/objetivo/<int:id>", methods=["GET"])
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

@app.route("/api/objetivo", methods=["POST"])
def criar_objetivo():
    try:
        data = request.get_json()
        cursor = conn.cursor()

        cursor.execute(
            f"""INSERT INTO T_VB_OBJETIVO 
            (ID_OBJETIVO, 
            NM_OBJETIVO, 
            PESO_OBJETIVO, 
            TEMPO_OBJETIVO,
            DT_CADASTRO,
            NM_USUARIO) 
            VALUES (
                SQ_VB_OBJETIVO.nextval, 
                '{data['nome']}', 
                {data['peso']}, 
                TO_DATE('{data['tempo']}', 'DD/MM/YYYY'),
                SYSDATE,
                USER)"""
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
    
@app.route("/api/objetivo/<int:id>", methods=["PUT"])
def atualizar_objetivo(id):
    try:
        data = request.get_json()
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



# MEDIDA   MEDIDA   MEDIDA   MEDIDA   MEDIDA
# MEDIDA   MEDIDA   MEDIDA   MEDIDA   MEDIDA
@app.route("/api/medida", methods=["GET"])
def get_all_medida():
    try:
        cursor = conn.cursor()
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

@app.route("/api/medida/<int:id>", methods=["GET"])
def get_medida_by_id(id):
    try:
        cursor = conn.cursor()
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

@app.route("/api/medida", methods=["POST"])
def criar_medida():
    try:
        data = request.get_json()
        cursor = conn.cursor()
        print(data)

        cursor.execute(
            f"""INSERT INTO T_VB_MEDIDA 
            (ID_MEDIDA, 
            CINTURA_MEDIDA, 
            TORAX_MEDIDA, 
            BRACO_DIREITO_MEDIDA, 
            BRACO_ESQUERDO_MEDIDA, 
            COXA_DIREITA_MEDIDA, 
            COXA_ESQUERDA_MEDIDA, 
            PANTURRILHA_DIREITA_MEDIDA, 
            PANTURRILHA_ESQUERDA_MEDIDA, 
            ALTURA_MEDIDA, 
            PESO_MEDIDA, 
            DT_CADASTRO, 
            NM_USUARIO) 
            VALUES (
                SQ_VB_MEDIDA.nextval, 
                {data['cintura']}, 
                {data['torax']}, 
                {data['braco_direito']}, 
                {data['braco_esquerdo']}, 
                {data['coxa_direita']}, 
                {data['coxa_esquerda']}, 
                {data['panturrilha_direita']}, 
                {data['panturrilha_esquerda']}, 
                {data['altura']}, 
                {data['peso']}, 
                SYSDATE, 
                USER)"""
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

@app.route("/api/medida/<int:id>", methods=["PUT"])
def atualizar_medida(id):
    try:
        data = request.get_json()
        cursor = conn.cursor()

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




# BIOTIPO   BIOTIPO   BIOTIPO   BIOTIPO   BIOTIPO
# BIOTIPO   BIOTIPO   BIOTIPO   BIOTIPO   BIOTIPO
@app.route("/api/biotipo", methods=["GET"])
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

@app.route("/api/biotipo/<int:id>", methods=["GET"])
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




# DIETA   DIETA   DIETA   DIETA   DIETA
# DIETA   DIETA   DIETA   DIETA   DIETA
@app.route("/api/dieta", methods=["GET"])
def get_all_dieta():
    try:
        cursor = conn.cursor()
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
    
@app.route("/api/dieta/<int:id>", methods=["GET"])
def get_dieta_by_id(id):
    try:
        cursor = conn.cursor()
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



# TREINO   TREINO   TREINO   TREINO   TREINO
# TREINO   TREINO   TREINO   TREINO   TREINO
@app.route("/api/treino", methods=["GET"])
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

@app.route("/api/treino/<int:id>", methods=["GET"])
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



# TIPO TREINO   TIPO TREINO   TIPO TREINO   TIPO TREINO   TIPO TREINO
# TIPO TREINO   TIPO TREINO   TIPO TREINO   TIPO TREINO   TIPO TREINO
@app.route("/api/tipo-treino", methods=["GET"])
def get_all_tipo_treino():
    try:
        cursor = conn.cursor()
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

@app.route("/api/tipo-treino/<int:id>", methods=["GET"])
def get_tipo_treino_by_id(id):
    try:
        cursor = conn.cursor()
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

@app.route("/api/tipo-treino/treino/<int:id>", methods=["GET"])
def get_tipo_treino_by_treino(id):
    try:
        cursor = conn.cursor()
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




# EXERCICIOS  EXERCICIOS   EXERCICIOS   EXERCICIOS   EXERCICIOS
# EXERCICIOS  EXERCICIOS   EXERCICIOS   EXERCICIOS   EXERCICIOS
@app.route("/api/exercicio", methods=["GET"])
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

@app.route("/api/exercicio/<int:id>", methods=["GET"])
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


@app.route("/api/exercicio/tipo-treino/<int:id>", methods=["GET"])
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



app.run(debug=True)