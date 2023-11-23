import requests
from datetime import datetime

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
            print("\n\nJSON", responseObjetivoJson, "\n\n")

            medidaSend = {"cintura": 0, "torax": 0, "braco_direito": 0, "braco_esquerdo": 0, "coxa_direita": 0, "coxa_esquerda": 0, "panturrilha_direita": 0, "panturrilha_esquerda": 0, "altura": altura, "peso": peso}
            responseMedida = requests.post('http://127.0.0.1:5000/api/medida', json=medidaSend)
            responseMedidaJson = responseMedida.json()
            print("\n\nJSON", responseMedidaJson, "\n\n")

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
            print("\n\nJSON", usuarioSend, "\n\n")

            responseCliente = requests.post('http://127.0.0.1:5000/api/cliente', json=usuarioSend)
            
            if responseCliente.status_code == 201:
                responseClienteJson = responseCliente.json()
                print("\nCadastro realizado com sucesso!\n")
                print("JSON", responseClienteJson)
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
        print("Deseja fazer login ? \n[1] - Sim \n[2] - Não")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            usuario = { "email_cliente": email, "senha_cliente": senha }
            
            if(email == "" or senha == ""):
                print("\nEmail ou Senha Incompletos!\n")
            else:
                response = requests.post('http://127.0.0.1:5000/api/cliente/login', json=usuario)
                if response.status_code == 200:
                    responseJson = response.json()
                    print("\nLogin realizado com sucesso!\n")
                    print("JSON", responseJson)
                    return responseJson
                else:
                    print("\nEmail ou senha inválidos!\n")
        elif opcao == 2:
            inicio()
        else:
            print("\nOpção inválida!\n")


def perfil(usuario):
    print("\n\n===ENTRANDO NA PÁGINA DE PERFIL===\n")
    print("O que você deseja fazer? \n[1] - Alterar Dados \n[2] - Alterar Medidas \n[3] - Alterar Objetivo \n[4] - Alterar Treino \n[5] - Alterar Dieta \n[6] - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print("\n\n===ENTRANDO NA PÁGINA DE ALTERAÇÃO DE DADOS===\n")
        print("O que você deseja alterar? \n[1] - Nome \n[2] - Email \n[3] - Senha \n[4] - Idade \n[5] - Sexo \n[6] - Voltar")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            nome = input("Digite seu nome: ")
            usuario['nm_cliente'] = nome
            response = requests.put('http://127.0.0.1:5000/api/cliente', json=usuario)
            if response.status_code == 200:
                responseJson = response.json()
                print("\nNome alterado com sucesso!\n")
                print("JSON", responseJson)
                perfil(responseJson)
            else:
                print("\nErro ao alterar nome!\n")






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


inicio()