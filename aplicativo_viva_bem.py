import requests
from datetime import datetime
import json

def validar_data(tempo):
    try:
        data = datetime.strptime(tempo, '%d/%m/%Y')
        return True, data.strftime('%d/%m/%Y')
    except ValueError:
        return False, None

def calcular_metabolismo(idade, sexo, peso, altura, frequencia_treino):
    if sexo == "Masculino":
        metabolismo = 66.5 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    elif sexo == "Feminino":
        metabolismo = 655.1 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

    metabolismo = metabolismo * frequencia_treino
    return metabolismo

def descobrir_biotipo():
    print("\n\n- Pegue sua mão direita e veja o tamanho do seu pulso")
    print("- Com o dedo indicador e o polegar da mão esquerda, envolva o pulso da mão direita")
    print("- Se os dedos se sobrepuseram, você é um ectomorfo")
    print("- Se os dedos se tocaram, você é um mesomorfo")      
    print("- Se os dedos não se tocaram, você é um endomorfo\n\n")
    input("Clique em qualquer tecla para continuar o cadastro...\n\n")

    


def cadastro():
    print("\n\n===ENTRANDO NA PÁGINA DE CADASTRO===\n")
    nome = input("Digite seu nome: ")
    while(True):
        email = input("Digite seu email: ")
        respostaEmail = requests.get('http://127.0.0.1:5000/api/cliente/' + email)
        if respostaEmail.status_code == 200:
            print("\nEmail já cadastrado!\n")
        else:
            break
    idade = int(input(("Digite sua idade: ")))
    while(True):
        print("Escolha seu sexo: \n1 - Masculino \n2 - Feminino")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            sexo = "Masculino"
            break
        elif opcao == 2:
            sexo = "Feminino"
            break
        else:
            print("\nOpção inválida!\n")
    senha = input("Digite sua senha: ")

    print("\n\n===MUDANDO PARA PRÓXIMA PÁGINA===\n")
    while(True):
        print("Escolha o seu objetivo:  \n[1] - Perder Gordura  \n[2] - Ganhar Músculo")
        objetivo = int(input("Escolha uma opção: "))
        if objetivo == 1:
            objetivo = "Perder Gordura"
            break
        elif objetivo == 2:
            objetivo = "Ganhar Músculo"
            break
        else:
            print("\nOpção inválida!\n")
    while(True):
        tempo = input("Digite uma data para atingir sua meta: (dia/mês/ano) -> ")
        valido, tempo = validar_data(tempo)
        if valido:
            data_tempo = tempo
            break
        else:
            print("\nData inválida!\n")
    while(True):
        print("Escolha sua frequência de treino: \n[1] - 1 a 2 vezes por semana \n[2] - 3 a 4 vezes por semana \n[3] - 5 a 6 vezes por semana")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            frequencia_treino = 1.2
            break
        elif opcao == 2:
            frequencia_treino = 1.55
            break
        elif opcao == 3:
            frequencia_treino = 1.9
            break
        else:
            print("\nOpção inválida!\n")
    peso = float(input("Digite sua meta de peso em kg: "))
    tempo = validar_data(tempo)
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em cm: "))
    metabolismo = calcular_metabolismo(idade, sexo, peso, altura, frequencia_treino)

    print("\n\n===MUDANDO PARA PRÓXIMA PÁGINA===\n")
    while(True):
        print("Escolha o seu biotipo corporal:  \n[1] - Ectomorfo  \n[2] - Mesomorfo \n[3] - Endomorfo \n[4] - Descobrir meu biotipo")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            biotipo = "Ectomorfo"
            break
        elif opcao == 2:
            biotipo = "Mesomorfo"
            break
        elif opcao == 3:
            biotipo = "Endomorfo"
            break
        elif opcao == 4:
            descobrir_biotipo()
        else:
            print("\nOpção inválida!\n")

    print("\n\n===MUDANDO PARA PRÓXIMA PÁGINA===\n")
    print("Selecione seu treino:  \n[1] - Treino Iniciante  \n[2] - Treino Intermediário \n[3] - Treino Avançado")
    while(True):
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            treino = "Treino Iniciante"
            break
        elif opcao == 2:
            treino = "Treino Intermediário"
            break
        elif opcao == 3:
            treino = "Treino Avançado"
            break
        else:
            print("\nOpção inválida!\n")
    
    print("\n\n===FINALIZANDO CADASTRO===\n")
    print("Ficha de Cadastro: \n")
    print("Nome: ", nome)
    print("Email: ", email)
    print("Idade: ", idade)
    print("Sexo: ", sexo)
    print("Senha: ", senha)
    print("\nObjetivo: ", objetivo)
    print("Meta de Peso: ", peso)
    print("Meta de Tempo: ", data_tempo)
    print("\nPeso: ", peso)
    print("Altura: ", altura)
    print("Metabolismo: ", metabolismo)
    print("Biotipo: ", biotipo)
    print("\nTreino: ", treino)
    print("\n\nDeseja confirmar o cadastro? \n[1] - Sim \n[2] - Não")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        try:
            objetivoSend = {"nome": objetivo, "peso": peso, "tempo": data_tempo}
            responseObjetivo = requests.post('http://127.0.0.1:5000/api/objetivo', json=objetivoSend)
            responseObjetivoJson = responseObjetivo.json()

            medidaSend = {"cintura": 0, "torax": 0, "braco_direito": 0, "braco_esquerdo": 0, "coxa_direita": 0, "coxa_esquerda": 0, "panturrilha_direita": 0, "panturrilha_esquerda": 0, "altura": altura, "peso": peso}
            responseMedida = requests.post('http://127.0.0.1:5000/api/medida', json=medidaSend)
            responseMedidaJson = responseMedida.json()

            usuarioSend = {
                "id_medida": responseMedidaJson['medida']['id'],
                "id_objetivo": responseObjetivoJson['objetivo']['id'],
                "id_biotipo": 1 if biotipo == "Ectomorfo" else 2 if biotipo == "Mesomorfo" else 3,
                "id_dieta": 1 if objetivo == "Perder Gordura" else 2,
                "id_treino": 1 if treino == "Treino Iniciante" else 2 if treino == "Treino Intermediário" else 3,
                "email_cliente": email,
                "senha_cliente": senha,
                "nm_cliente": nome,
                "genero_cliente": sexo,
                "idade_cliente": idade,
                "metabolismo_cliente": metabolismo
            }
            responseCliente = requests.post('http://127.0.0.1:5000/api/cliente', json=usuarioSend)
            
            if responseCliente.status_code == 201:
                responseClienteJson = responseCliente.json()
                print("\nCadastro realizado com sucesso!\n")
                inicio()
            else:
                print(f"Erro: Status Code Cliente {responseCliente.status_code}.")
                print("Erro no cadastro: ", responseCliente.text)
        except Exception as e:
            print("Erro no cadastro: ", e)
    elif opcao == 2:
        print("Cadastro cancelado!")
    else:
        print("\nOpção inválida!\n")


def login():
    print("\n\n===ENTRANDO NA PÁGINA DE LOGIN===\n")
    while(True):
        email = input("\nDigite seu email: ")
        senha = input("Digite sua senha: ")
        usuario = { "email_cliente": email, "senha_cliente": senha }
        
        if(email == "" or senha == ""):
            print("\nEmail ou Senha Incompletos!\n")
            continue
        else:
            response = requests.post('http://127.0.0.1:5000/api/cliente/login', json=usuario)
            if response.status_code == 200:
                responseJson = response.json()
                print("\nLogin realizado com sucesso!\n")
                return responseJson
            else:
                print("\nEmail ou senha inválidos!\n")
                continue


def editar_perfil(usuario):
    while(True):
        opcao_perfil = int(input(("\n\nQuais dados você deseja alterar? \n[1] - Nome \n[2] - Email \n[3] - Senha \n[4] - Idade \n[5] - Sexo \n[6] - Voltar \nEscolha uma opção: ")))

        if opcao_perfil not in range(1, 6):
            print("Opção inválida. Tente novamente.")
            continue

        if opcao_perfil == 6: 
            inicio()

        if opcao_perfil == 1:
            print("\n\nNome atual: ", usuario['nm_cliente'])
            novo_valor = input("\nDigite o novo nome: ")
            usuario['nm_cliente'] = novo_valor
        elif opcao_perfil == 2:
            print("\n\nEmail atual: ", usuario['email_cliente'])
            while(True):
                novo_valor = input("\nDigite o novo email: ")
                respostaEmail = requests.get('http://127.0.0.1:5000/api/cliente/' + novo_valor)
                if respostaEmail.status_code == 200:
                    print("\nEmail já cadastrado!\n")
                else:
                    break
        elif opcao_perfil == 3:
            print("\n\nSenha atual: ", usuario['senha_cliente'])
            novo_valor = input("\nDigite a nova senha: ")
            usuario['senha_cliente'] = novo_valor
        elif opcao_perfil == 4:
            print("\n\nIdade atual: ", usuario['idade_cliente'])
            novo_valor = input("\nDigite a nova idade: ")
            usuario['idade_cliente'] = int(novo_valor)
        elif opcao_perfil == 5:
            print("\n\nSexo atual: ", usuario['genero_cliente'])
            while(True):
                print("\nEscolha seu sexo: \n1 - Masculino \n2 - Feminino")
                opcao_sexo = int(input("Escolha uma opção: "))
                if opcao_sexo == 1:
                    novo_valor = "Masculino"
                    break
                elif opcao_sexo == 2:
                    novo_valor = "Feminino"
                    break
                else:
                    print("\nOpção inválida!\n")
            usuario['genero_cliente'] = novo_valor

        decisao_atualizar = int(input("\n\nDeseja atualizar mais algum dado? \n[1] - Sim \n[2] - Não \n> "))
        if decisao_atualizar == 2:
            break

    id_cliente = usuario.get('id_cliente')
    usuario.pop('id_cliente', None)
    response = requests.put('http://127.0.0.1:5000/api/cliente/' + str(id_cliente), json=usuario)

    if response.status_code == 200:
        responseJson = response.json()
        print("\n\Cliente Atualizado com Sucesso!\n\n")
        perfil(responseJson['cliente'])
    else:
        print("\nErro ao alterar o cliente!\n")


def editar_objetivo(response_objetivo_json, usuario):
    while(True):
        print("\n\nO que você deseja alterar no seu objetivo? \n[1] - Nome \n[2] - Peso \n[3] - Tempo \n[4] - Voltar\n")
        opcao_objetivo = int(input("Escolha uma opção: "))

        if opcao_objetivo not in range(1, 4):
            print("Opção inválida. Tente novamente.")
            continue

        if opcao_objetivo == 4: 
            perfil(usuario)

        if opcao_objetivo == 1:
            print("\n\nNome atual: ", response_objetivo_json['nome'])
            novo_nome_objetivo = int(input("\nEscolha um novo nome: \n[1] - Perder Gordura \n[2] - Ganhar Músculo \n> "))
            if novo_nome_objetivo == 1:
                response_objetivo_json['nome'] = "Perder Gordura"
            elif novo_nome_objetivo == 2:
                response_objetivo_json['nome'] = "Ganhar Músculo"
            else:
                print("\nOpção inválida!\n")
                continue
        elif opcao_objetivo == 2:
            print("\n\nPeso atual: ", response_objetivo_json['peso'])
            novo_valor = input("\nDigite o novo peso: ")
            response_objetivo_json['peso'] = float(novo_valor)
        elif opcao_objetivo == 3:
            print("\n\nTempo atual: ", response_objetivo_json['tempo'])
            while(True):
                novo_valor = input("\nDigite o novo tempo: (dia/mês/ano) -> ")
                valido, tempo = validar_data(novo_valor)
                if valido:
                    response_objetivo_json['tempo'] = tempo
                    break
                else:
                    print("\nData inválida!\n")

        decisao_atualizar = int(input("\n\nDeseja atualizar mais algum dado? \n[1] - Sim \n[2] - Não \n> "))
        if decisao_atualizar == 2:
            break

    id_objetivo = response_objetivo_json.get('id')
    response_objetivo_json.pop('id', None)
    print("ID do objetivo: ", id_objetivo)
    print(response_objetivo_json)
    response = requests.put('http://127.0.0.1:5000/api/objetivo/' + str(id_objetivo), json=response_objetivo_json)

    if response.status_code == 200:
        print("\n\Objetivo Atualizado com Sucesso!\n\n")
        perfil(usuario)
    else:
        print("\nErro ao alterar o objetivo!\n")


def editar_medida(response_medida_json, usuario):
    while(True):
        print("\n\nO que você deseja alterar? \n[1] - Cintura \n[2] - Tórax \n[3] - Braço Direito \n[4] - Braço Esquerdo \n[5] - Coxa Direita \n[6] - Coxa Esquerda \n[7] - Panturrilha Direita \n[8] - Panturrilha Esquerda \n[9] - Altura \n[10] - Peso \n[11] - Voltar\n")
        opcao_medida = int(input("Escolha uma opção: "))

        if int(opcao_medida) not in range(1, 11):
            print("Opção inválida. Tente novamente.")
            continue

        if(opcao_medida == 11):
            perfil(usuario)
            
        if(opcao_medida == 1):
            print("\n\nCintura atual: ", response_medida_json['cintura'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['cintura'] = float(novo_valor)
        elif(opcao_medida == 2):
            print("\n\nTórax atual: ", response_medida_json['torax'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['torax'] = float(novo_valor)
        elif(opcao_medida == 3):
            print("\n\nBraço Direito atual: ", response_medida_json['braco_direito'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['braco_direito'] = float(novo_valor)
        elif(opcao_medida == 4):
            print("\n\nBraço Esquerdo atual: ", response_medida_json['braco_esquerdo'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['braco_esquerdo'] = float(novo_valor)
        elif(opcao_medida == 5):
            print("\n\nCoxa Direita atual: ", response_medida_json['coxa_direita'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['coxa_direita'] = float(novo_valor)
        elif(opcao_medida == 6):
            print("\n\nCoxa Esquerda atual: ", response_medida_json['coxa_esquerda'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['coxa_esquerda'] = float(novo_valor)
        elif(opcao_medida == 7):
            print("\n\nPanturrilha Direita atual: ", response_medida_json['panturrilha_direita'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['panturrilha_direita'] = float(novo_valor)
        elif(opcao_medida == 8):
            print("\n\nPanturrilha Esquerda atual: ", response_medida_json['panturrilha_esquerda'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['panturrilha_esquerda'] = float(novo_valor)
        elif(opcao_medida == 9):
            print("\n\nAltura atual: ", response_medida_json['altura'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['altura'] = float(novo_valor)
        elif(opcao_medida == 10):
            print("\n\nPeso atual: ", response_medida_json['peso'])
            novo_valor = input("\nDigite a nova medida: ")
            response_medida_json['peso'] = float(novo_valor)
        
        decisao_atualizar = int(input("\n\nDeseja atualizar mais algum dado? \n[1] - Sim \n[2] - Não \n> "))
        if decisao_atualizar == 2:
            break

    id_medida = response_medida_json.get('id')
    response_medida_json.pop('id', None)
    response = requests.put('http://127.0.0.1:5000/api/medida/' + str(id_medida), json=response_medida_json)

    if response.status_code == 200:
        print("\n\Medida Atualizada com Sucesso!\n\n")
        perfil(usuario)
    else:
        print("\nErro ao alterar a medida!\n")


def editar_dieta(response_dieta_json, usuario):
    while(True):
        print("\n\nO que você deseja alterar? \n[1] - Dieta \n[2] - Voltar\n")
        opcao_dieta = int(input("Escolha uma opção: "))

        if opcao_dieta not in range(1, 3):
            print("Opção inválida. Tente novamente.")
            continue

        if(opcao_dieta == 1):
            print("\n\nDieta atual: ", response_dieta_json['nome'])
            novo_valor = int(input("\nEscolha uma nova dieta: \n[1] - Dieta de Emagrecimento \n[2] - Dieta de Ganho de Massa \n> "))
            if novo_valor == 1:
                usuario['id_dieta'] = 1
            elif novo_valor == 2:
                usuario['id_dieta'] = 2
            else:
                print("\nOpção inválida!\n")
                continue

        decisao_atualizar = int(input("\n\nDeseja atualizar mais algum dado? \n[1] - Sim \n[2] - Não \n> "))
        if decisao_atualizar == 2:
            break

    id_cliente = usuario.get('id_cliente')
    usuario.pop('id_cliente', None)
    response = requests.put('http://127.0.0.1:5000/api/cliente/' + str(id_cliente), json=usuario)

    if response.status_code == 200:
        responseJson = response.json()
        print("\n\Dieta Atualizada com Sucesso!\n\n")
        perfil(responseJson['cliente'])
    else:
        print("\nErro ao alterar a dieta!\n")


def editar_treino(response_treino_json, usuario):
    while(True):
        print("\n\nO que você deseja alterar? \n[1] - Treino \n[2] - Voltar\n")
        opcao_treino = int(input("Escolha uma opção: "))

        if opcao_treino not in range(1, 3):
            print("Opção inválida. Tente novamente.")
            continue

        if(opcao_treino == 1):
            print("\n\nTreino atual: ", response_treino_json['nome'])
            novo_valor = int(input("\nEscolha um novo treino: \n[1] - Treino Iniciante \n[2] - Treino Intermediário \n[3] - Treino Avançado \n> "))
            if novo_valor == 1:
                usuario['id_treino'] = 1
            elif novo_valor == 2:
                usuario['id_treino'] = 2
            elif novo_valor == 3:
                usuario['id_treino'] = 3
            else:
                print("\nOpção inválida!\n")
                continue

        decisao_atualizar = int(input("\n\nDeseja atualizar mais algum dado? \n[1] - Sim \n[2] - Não \n> "))
        if decisao_atualizar == 2:
            break
    
    id_cliente = usuario.get('id_cliente')
    usuario.pop('id_cliente', None)
    response = requests.put('http://127.0.0.1:5000/api/cliente/' + str(id_cliente), json=usuario)

    if response.status_code == 200:
        responseJson = response.json()
        print("\n\Treino Atualizado com Sucesso!\n\n")
        perfil(responseJson['cliente'])
    else:
        print("\nErro ao alterar o treino!\n")


def remover_perfil(usuario):
    print("\n\n===ENTRANDO NA PÁGINA DE REMOÇÃO DE PERFIL===\n")
    print("Nome: ", usuario['nm_cliente'])
    print("Email: ", usuario['email_cliente'])
    print("Idade: ", usuario['idade_cliente'])
    print("Sexo: ", usuario['genero_cliente'])
    print("Senha: ", usuario['senha_cliente'])

    confirmar = int(input("\n\nDeseja realmente remover seu perfil? \n[1] - Sim \n[2] - Não \n> "))

    if(confirmar == 1):
        print("\n\n===REMOVENDO PERFIL===\n")
        responseDelete = requests.delete('http://127.0.0.1:5000/api/cliente/' + str(usuario['id_cliente']))
        
        if(responseDelete.status_code == 200):
            print("\nPerfil deletado com sucesso!\n")
            inicio()
    
    elif(confirmar == 2):
        print("\n\n===VOLTANDO PARA O PERFIL===\n")
        perfil(usuario)


def exportar_json_treinos(usuario):
    print("\n\n===ENTRANDO NA PÁGINA DE EXPORTAÇÃO DE JSON DOS TREINOS===\n")

    exercicios_export_json = []

    response_treino = requests.get('http://127.0.0.1:5000/api/tipo-treino/treino/' + str(usuario['id_treino']))
    response_treino_json = response_treino.json()

    for tipo_treino in response_treino_json:
        response_exercicios = requests.get('http://127.0.0.1:5000/api/exercicio/tipo-treino/' + str(tipo_treino['id_tipo_treino']))
        response_exercicios_json = response_exercicios.json()

        exercicios_export_json.extend(response_exercicios_json)

    with open('exercicios_exportados.json', 'w') as json_file:
        json.dump(exercicios_export_json, json_file, indent=2)

    print("\n\nExportação concluída. Os exercícios foram exportados para o arquivo exercicios_exportados.json.\n\n")
    perfil(usuario)






def perfil(usuario):
    print("\n\n===ENTRANDO NA PÁGINA DE PERFIL===\n")

    print("Nome: ", usuario['nm_cliente'])
    print("Email: ", usuario['email_cliente'])
    print("Idade: ", usuario['idade_cliente'])
    print("Sexo: ", usuario['genero_cliente'])
    print("Senha: ", usuario['senha_cliente'])

    response_objetivo = requests.get('http://127.0.0.1:5000/api/objetivo/' + str(usuario['id_objetivo']))
    response_objetivo_json = response_objetivo.json()
    print("\nObjetivo: ", response_objetivo_json['nome'])
    print("Meta de Peso: ", response_objetivo_json['peso'])
    print("Meta de Tempo: ", response_objetivo_json['tempo'])

    response_medida = requests.get('http://127.0.0.1:5000/api/medida/' + str(usuario['id_medida']))
    response_medida_json = response_medida.json()
    print("\nPeso: ", response_medida_json['peso'])
    print("Altura: ", response_medida_json['altura'])
    print("Metabolismo: ", usuario['metabolismo_cliente'])

    response_biotipo = requests.get('http://127.0.0.1:5000/api/biotipo/' + str(usuario['id_biotipo']))
    response_biotipo_json = response_biotipo.json()
    print("Biotipo: ", response_biotipo_json['nome'])

    response_treino = requests.get('http://127.0.0.1:5000/api/treino/' + str(usuario['id_treino']))
    response_treino_json = response_treino.json()
    print("\nTreino: ", response_treino_json['nome'])

    response_dieta = requests.get('http://127.0.0.1:5000/api/dieta/' + str(usuario['id_dieta']))
    response_dieta_json = response_dieta.json()
    print("\nDieta: ", response_dieta_json['nome'])

    opcao_acao = int(input("\n\nDESEJA REALIZAR QUE AÇÃO EM SEU PERFIL: \n[1] - Acessar Treino \n[2] - Acessar Dieta \n[3] - Alterar Dados \n[4] - Deletar Perfil \n[5] - Exportar JSON dos treinos \n[6] - Sair \n> "))

    if opcao_acao == 1:
        print("\n\n===ENTRANDO NA PÁGINA DE TREINO===\n\n")
        print("Treino: ", response_treino_json['nome'].upper())
        print("Descrição: ", response_treino_json['descricao'])

        response_tipo_treino = requests.get('http://127.0.0.1:5000/api/tipo-treino/treino/' + str(usuario['id_treino']))
        response_tipo_treino_json = response_tipo_treino.json()

        for tipo_treino in response_tipo_treino_json:
            print(f"\n[{tipo_treino['id_tipo_treino']}] - Tipo de Treino: ", tipo_treino['nome_tipo_treino'])
            print("      Descrição: ", tipo_treino['descricao_tipo_treino'])

        tipo_treino_escolhido = int(input("\n\nEscolha um tipo de treino:"))

        response_exercicios = requests.get('http://127.0.0.1:5000/api/exercicio/tipo-treino/' + str(tipo_treino_escolhido))
        response_exercicios_json = response_exercicios.json()

        for exercicio in response_exercicios_json:
            print(f"\nExercício: ", exercicio['nome'])
            print("Repetições: ", exercicio['repeticoes'])
            print("Séries: ", exercicio['series'])
            print("Tempo de Descanso: ", exercicio['tempo_descanso'] , " minutos")
        
        voltar = int(input("\n\nVoltar para: \n[1] - Perfil \n[2] - Menu Principal \n> "))
        if voltar == 1:
            perfil(usuario)
        elif voltar == 2:
            inicio()

    if opcao_acao == 2:
        print("\n\n=== ENTRANDO NA PÁGINA DE DIETA ===\n\n")
        print("Dieta: ", response_dieta_json['nome'])

        if usuario['id_dieta'] == 1:
            descricao_dieta = response_dieta_json['descricao']['dieta_emagrecimento']
        elif usuario['id_dieta'] == 2:
            descricao_dieta = response_dieta_json['descricao']['dieta_musculo']

        print("\n\n=== EXIBINDO DETALHES DA DIETA ===\n")

        for refeicao, opcoes in descricao_dieta.items():
            print(f"\n\n{refeicao.upper()}\n")
            for opcao in opcoes:
                print(f"Opção: {opcao['opcao']}")
                print(f"Calorias: {opcao['calorias']}")
                print(f"Carboidratos: {opcao['carboidratos']}")
                print(f"Gorduras: {opcao['gorduras']}")
                print(f"Proteínas: {opcao['proteinas']}\n")

        voltar = int(input("\n\nVoltar para: \n[1] - Perfil \n[2] - Menu Principal \n> "))
        if voltar == 1:
            perfil(usuario)
        elif voltar == 2:
            inicio()

    if opcao_acao == 3:
        while True:
            print("\n\n===ENTRANDO NA PÁGINA DE ALTERAÇÃO DE DADOS===")
            opcao_update = int(input("\nO que você deseja alterar? \n\n[1] - Perfil \n[2] - Objetivo \n[3] - Medidas \n[4] - Dietas \n[5] - Treinos \n[6] - Sair \n> "))

            if opcao_update == 1:
                editar_perfil(usuario)
                break
            elif opcao_update == 2:
                editar_objetivo(response_objetivo_json, usuario)
                break
            elif opcao_update == 3:
                editar_medida(response_medida_json, usuario)
            elif opcao_update == 4:
                editar_dieta(response_dieta_json, usuario)
            elif opcao_update == 5:
                editar_treino(response_treino_json, usuario)
            elif opcao_update == 6:
                perfil(usuario)
                break
        
    if opcao_acao == 4:
        remover_perfil(usuario)

    if opcao_acao == 5:
        exportar_json_treinos(usuario)

    if opcao_acao == 6:
        print("\n===SAINDO DO PERFIL DO USUÁRIO===\n\n")
        inicio()





def inicio():
    print("\n\nBem vindo ao Viva Bem!")
    print("O que você deseja fazer?")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastro()
    elif opcao == 2:
        usuario = login()
        print("Bem Vindo ", usuario['nm_cliente'].upper())
        perfil(usuario)
    elif opcao == 3:
        print("Obrigado por usar o Viva Bem!")
    else: 
        print("Opção inválida!")
        inicio()


inicio()