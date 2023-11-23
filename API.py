import oracledb
from flask import Flask, jsonify, request

conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")

app = Flask(__name__)


@app.route("/api/cliente", methods=["GET"])
def get_all_cliente():
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
            "dt_cadastro": cliente[12].strftime("%Y-%m-%d %H:%M:%S"),
            "nm_usuario": cliente[13],
        }
        clientes_json.append(cliente_dict)

    return jsonify(clientes_json)


@app.route("/api/cliente/<int:id>", methods=["GET"])
def get_cliente_by_id(id):
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
        "dt_cadastro": cliente[12].strftime('%Y-%m-%d %H:%M:%S'),
        "nm_usuario": cliente[13]
    }

    return jsonify(cliente_dict)


@app.route("/api/cliente/<string:email>", methods=["GET"])
def get_cliente_by_email(email):
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
        "dt_cadastro": cliente[12].strftime('%Y-%m-%d %H:%M:%S'),
        "nm_usuario": cliente[13]
    }

    return jsonify(cliente_dict)


@app.route("/api/cliente/login", methods=["POST"])
def login_cliente():
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM T_VB_CLIENTE WHERE EMAIL_CLIENTE = '{data['email_cliente']}' AND SENHA_CLIENTE = '{data['senha_cliente']}'"
    )
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
        "dt_cadastro": cliente[12].strftime('%Y-%m-%d %H:%M:%S'),
        "nm_usuario": cliente[13]
    }

    return jsonify(cliente_dict)


@app.route("/api/cliente", methods=["POST"])
def criar_cliente():
    data = request.get_json()
    cursor = conn.cursor()

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
    return jsonify({"message": "Cliente criado com sucesso!"}), 201







# OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO
# OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO   OBJETIVO

@app.route("/api/objetivo", methods=["GET"])
def get_all_objetivo():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM T_VB_OBJETIVO ORDER BY 1 ASC")
    objetivos = cursor.fetchall()

    if len(objetivos) == 0:
        return jsonify({"message": "Nenhum objetivo encontrado!"}), 404

    objetivos_json = []
    for objetivo in objetivos:
        objetivo_dict = {
            "id_objetivo": objetivo[0],
            "nm_objetivo": objetivo[1],
            "peso_objetivo": objetivo[2],
            "tempo_objetivo": objetivo[3],
        }
        objetivos_json.append(objetivo_dict)

    return jsonify(objetivos_json)


@app.route("/api/objetivo/<int:id>", methods=["GET"])
def get_objetivo_by_id(id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM T_VB_OBJETIVO WHERE ID_OBJETIVO = {id}")
    objetivo = cursor.fetchone()

    if objetivo is None:
        return jsonify({"message": "Objetivo não encontrado!"}), 404
    
    objetivo_dict = {
        "id_objetivo": objetivo[0],
        "nm_objetivo": objetivo[1],
        "peso_objetivo": objetivo[2],
        "tempo_objetivo": objetivo[3],
    }

    return jsonify(objetivo_dict)


@app.route("/api/objetivo", methods=["POST"])
def criar_objetivo():
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
    cursor.execute(f"SELECT * FROM T_VB_OBJETIVO WHERE NM_OBJETIVO = '{data['nome']}' AND PESO_OBJETIVO = {data['peso']} AND TEMPO_OBJETIVO = TO_DATE('{data['tempo']}', 'DD/MM/YYYY')")
    objetivo = cursor.fetchone()
    return jsonify({ "message": "Objetivo criado com sucesso!", "objetivo": objetivo }), 201


@app.route("/api/objetivo/<int:id>", methods=["PUT"])
def atualizar_objetivo(id):
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








# MEDIDA   MEDIDA   MEDIDA   MEDIDA   MEDIDA
# MEDIDA   MEDIDA   MEDIDA   MEDIDA   MEDIDA

@app.route("/api/medida", methods=["GET"])
def get_all_medida():
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

    return jsonify(medidas_json) 


@app.route("/api/medida/<int:id>", methods=["GET"])
def get_medida_by_id(id):
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

    return jsonify(medida_dict)


@app.route("/api/medida", methods=["POST"])
def criar_medida():
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













app.run(debug=True)