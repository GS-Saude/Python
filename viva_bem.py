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
        print("\nDeseja fazer login ? \n[1] - Sim \n[2] - Não")
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

    opcao_acao = int(input("\n\nDESEJA REALIZAR QUE AÇÃO EM SEU PERFIL: \n[1] - Acessar Treino \n[2] - Acessar Dieta \n[3] - Alterar Dados \n[4] - Sair \n> "))

    if opcao_acao == 1:
        print("\n\n===ENTRANDO NA PÁGINA DE TREINO===\n\n")
        print("Treino: ", response_treino_json['nome'].upper())
        print("Descrição: ", response_treino_json['descricao'])

        response_tipo_treino = requests.get('http://127.0.0.1:5000/api/tipo-treino/treino/' + str(usuario['id_treino']))
        response_tipo_treino_json = response_tipo_treino.json()

        for tipo_treino in response_tipo_treino_json:
            print(f"\n[{tipo_treino['id_tipo_treino']}] - Tipo de Treino: ", tipo_treino['nome_tipo_treino'])
            print("      Descrição: ", tipo_treino['descricao_tipo_treino'])

        tipo_treino_escolhido = int(input("Escolha um tipo de treino:"))

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
        print("\n\n===ENTRANDO NA PÁGINA DE DIETA===\n\n")
        print("Dieta: ", response_dieta_json['nome'])
        print("Descrição: ", response_dieta_json['descricao'])

    if opcao_acao == 3:
        while True:
            print("\n\n===ENTRANDO NA PÁGINA DE ALTERAÇÃO DE DADOS===")
            print("O que você deseja alterar? \n[1] - Nome \n[2] - Email \n[3] - Senha \n[4] - Idade \n[5] - Sexo \n[6] - Voltar")
            opcao = input("Escolha uma opção: ")

            if int(opcao) not in range(1, 6):
                print("Opção inválida. Tente novamente.")
                continue

            opcao = int(opcao)

            if opcao == 6: 
                inicio()

            if opcao == 1:
                novo_valor = input("Digite o novo nome: ")
                usuario['nm_cliente'] = novo_valor
            elif opcao == 2:
                while(True):
                    novo_valor = input("Digite o novo email: ")
                    respostaEmail = requests.get('http://127.0.0.1:5000/api/cliente/' + novo_valor)
                    if respostaEmail.status_code == 200:
                        print("\nEmail já cadastrado!\n")
                    else:
                        break
                usuario['email_cliente'] = novo_valor
            elif opcao == 3:
                novo_valor = input("Digite a nova senha: ")
                usuario['senha_cliente'] = novo_valor
            elif opcao == 4:
                novo_valor = input("Digite a nova idade: ")
                usuario['idade_cliente'] = int(novo_valor)
            elif opcao == 5:
                while(True):
                    print("Escolha seu sexo: \n1 - Masculino \n2 - Feminino")
                    opcao = int(input("Escolha uma opção: "))
                    if opcao == 1:
                        novo_valor = "Masculino"
                        break
                    elif opcao == 2:
                        novo_valor = "Feminino"
                        break
                    else:
                        print("\nOpção inválida!\n")
                usuario['genero_cliente'] = novo_valor

            print("Usuario para atualizar: ", usuario)
            return
            response = requests.put('http://127.0.0.1:5000/api/cliente', json=usuario)

            if response.status_code == 200:
                responseJson = response.json()
                print("\nDados alterados com sucesso!\n")
                print("JSON", responseJson)
                perfil(responseJson)
            else:
                print("\nErro ao alterar dados!\n")

    if opcao_acao == 4:
        print("\n\n===SAINDO DO PERFIL DO USUÁRIO===")
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


inicio()