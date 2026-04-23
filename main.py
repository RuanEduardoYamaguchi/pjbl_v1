# variáveis globais

MENU_PRINCIPAL = '''Nosso programa tem varias funções, escolha qual você gostaria de calcular
[1] IMC
[2] Meta de Hidratação Diária
[3] Estimativa de Gasto Calórico
[4] Meta Diária de Exercício (tempo)
[5] Resumo Diário
[6] Calculo Gasto Calórico por Objetivo
[7] Calcular Para Novo Usuário
[8] Encerrar programa
Escolha uma função: '''

MENU_GASTO_CALORICO = """ Digite o número de uma atividade para calcular o gasto calórico
[1] Caminhada leve
[2] Corrida
[3] Musculação
[4] Bicicleta"""

MENU_NIVEL_DE_ATIVIDADE = '''Qual nivel de atividade você ira fazer:
[1] Sedentário
[2] Levemente ativo
[3] Moderado
[4] Muito ativo
Opção escolhida:'''

MENU_OBJETIVO_SELECIONADO = '''Qual o seu objetivo. Exemplo: 
[1] Emagrecer  
[2] Manter
[3] Ganhar massa
Objetivo: '''

MENU_EXERCICIO_SELECIONADO = '''Qual atividade você quer praticar: 
[1] Caminhada
[2] Corrida
[3] Musculação
Opção escolhida:'''

agua = 0
exercicio = 0
gasto_calorico_estimado= 0
tempo_treino_feito = 0
objetivo = "NA"
calorias = 0
tempo = 0
sexo = ""
meta_tempo_exercicios_diaria = 0
meta_diaria_exercicios_minutos = 0

print(f"{'=-'*10} Bem vindo ao FitCore {'=-'*10} \nA calculadora focada em seu desenvolvimento físico")
executar = str(input("Deseja iniciar o programa? [S/N]")).upper()
while executar != 'S' and executar != 'N':  # valida inicicio
    executar = str(input("Deseja iniciar o programa? [S/N]")).upper()

while executar == 'S':

    # captura de base de calculos
    sexo = str(input("Qual seu sexo biologico: [M/F]")).upper()
    while sexo != 'M' and sexo != 'F':  # valida sexo
        sexo = str(input("Algo deu errado, Digite o sexo novamente: [M/F]")).upper()

    idade = int(input("Qual a sua idade: "))
    while idade < 0:  # valida idade
        idade = int(input("Algo deu errado, Digite a idade novamente: "))

    peso = float(input('informe seu peso: '))
    while peso < 0:  # valida peso
        peso = float(input("Algo deu errado, Digite o peso novamente: "))

    altura = float(input('Agora informe a sua altura (exemplo: 1.75): '))
    while altura < 0 or altura > 3:  # valida altura
        altura = float(input("Algo deu errado, Digite a altura novamente (exemplo: 1.75): "))

    dados_validos = ''  # confirma dados de entrada
    while dados_validos != 'S' and dados_validos != 'N':
        print(f"Dados = sexo {sexo}, idade {idade}, peso {peso} e altura {altura}")
        dados_validos = str(input("Os Dados estao corretos: [S/N]")).upper()
    
    # Valida dados usuario
    if dados_validos == 'S':
        possui_usuario = 'S'
    else:
        possui_usuario = 'N'

    # Calculo imc e hidratação para uso no resumo diário.
    imc = peso / (altura * altura)
    agua = peso * 35

    # loop com dados do usuário
    while possui_usuario == 'S':

        opcao = int(input(MENU_PRINCIPAL))

        if opcao == 1:  # calculo IMC
            if imc >= 18.5 and imc <= 24.9:
                print(f"Seu IMC é: {imc:.2f}. Você está no seu peso ideal.")
            elif imc >= 25 and imc <= 29.9:
                print(f"Seu IMC é: {imc:.2f}. Você está com sobrepeso")
            elif imc <= 18.5:
                print(f"Seu IMC é: {imc:.2f}. Você está abaixo do peso ideal.")
            elif imc >= 30 and imc <=34.9:
                print(f"Seu IMC é: {imc:.2f}. Você está com obesidade grau I.")
            elif imc >= 35 and imc <=39.9:
                print(f"Seu IMC é: {imc:.2f}. Você está com obesidade grau II.")
            else: #quando for maior que 39.9
                print(f"Seu IMC é: {imc:.2f}. Você está com obesidade grau III.")
            print("VOLTANDO AO MENU PRINCIPAL... \n")

        elif opcao == 2:  # hidratação diária
            print(f"\nPara atingir sua meta diaria de hidratação, você precisa ingerir {agua} Ml de água \n")
            print("VOLTANDO AO MENU PRINCIPAL... \n")

        elif opcao == 3:  # estimativa de gasto calórico
            
            visualizar_menu_gasto_calorico = 'S'
            gasto_calorico_estimado= 0

            while visualizar_menu_gasto_calorico == 'S':
                print(MENU_GASTO_CALORICO)
                atividade = int(input("Opção: "))

                if atividade == 1:  # caminhada leve
                    tempo = int(input('Quantos minutos? '))
                    calorias = 3.5 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    gasto_calorico_estimado= gasto_calorico_estimado+ calorias
                
                elif atividade == 2:  # corrida
                    tempo = int(input('Quantos minutos? '))
                    calorias = 8 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    gasto_calorico_estimado= gasto_calorico_estimado+ calorias
                
                elif atividade == 3:  # musculação
                    tempo = int(input('Quantos minutos? '))
                    calorias = 7 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    gasto_calorico_estimado= gasto_calorico_estimado+ calorias
                
                elif atividade == 4: # bicicleta
                    tempo = int(input('Quantos minutos? '))
                    calorias = 7 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    gasto_calorico_estimado= gasto_calorico_estimado+ calorias
                
                else:
                    print("Atividade inválida.")

                print(f"Total acumulado: {gasto_calorico_estimado:.1f}")
                visualizar_menu_gasto_calorico = input('Adicionar outra atividade? [S/N]: ').upper()

            print("VOLTANDO AO MENU PRINCIPAL...")

        elif opcao == 4:  # calculo da meta diária de exercício - utilizando a recomendação da OMS
            exercicio_moderado = 300
            exercicio_alta_intensidade = 150

            print("Vamos calcular sua meta diária de exercício!")
            print("")
            qntd_dias_exercicio = int(input("Digite o nº de dias que você pretende se exercitar por semana. "))
            while qntd_dias_exercicio < 1 or qntd_dias_exercicio > 7: #validador de dias da semana
                print("Valor inválido. Digite o nº de dias que você pretende se exercitar por semana novamente. ")
                qntd_dias_exercicio = int(input("Digite a sua opção: "))

            print("Digite o nº da opção com a intensidade que você pretende realizar os exercícios: ")
            print("[1] Moderado")
            print("[2] Alta intensidade")
            intensidade_exercicio = int(input("Digite a sua opção: "))

            while intensidade_exercicio < 1 or intensidade_exercicio > 2: #validador de opção
                print("Valor inválido. Digite novamente nº da opção com a intensidade que você pretende realizar os exercícios:.")
                print("[1] Moderado")
                print("[2] Alta intensidade")
                intensidade_exercicio = float(input("Digite a sua opção: "))

            if intensidade_exercicio == 1:
                meta_diaria_exercicios_minutos = (exercicio_moderado / qntd_dias_exercicio)
                print("Sua meta diária é realizar:", meta_diaria_exercicios_minutos, "minutos de exercício durante", qntd_dias_exercicio, "dias da semana. ")
            else:
                meta_diaria_exercicios_minutos = (exercicio_alta_intensidade / qntd_dias_exercicio)
                print("Sua meta diária é realizar:", meta_diaria_exercicios_minutos, "minutos de exercício durante", qntd_dias_exercicio, "dias da semana. ")

        elif opcao == 5:  # Gera resumo diario
            print("Vamos para seu resumo diário\n",
                f"- O seu imc é: {imc:.2f}\n",
                f"- Meta diária de hidratação: {agua}mL\n",
                f"- Total de exercicios feitos: {exercicio}\n",
                f"- Total de calorias gastas: {gasto_calorico_estimado} kcal\n",
                f"- Meta de exercícios diária: {meta_tempo_exercicios_diaria}h\n",
                f"- Tempo de treino feito: {tempo_treino_feito}h\n",
                f"- Objetivo: {objetivo}",
                sep='')  # parâmetro separador do print
            iniciar = str(input("Gostaria de refazer os testes: [S/N]")).upper()

        elif opcao == 6: # meta diária de exercício, de acordo com o objetivo
            if sexo == "M":
                tmb = (10 * peso) + (6.25 * (altura * 100)) - (5 * idade) + 5
                print(f"Essa é a sua taxa metabólica basal: {tmb}")
            elif sexo == "F":
                tmb = (10 * peso) + (6.25 * (altura * 100)) - (5 * idade) - 161
                print(f"Essa é a sua taxa metabólica basal: {tmb}")

            nivel_atividade = int(input(MENU_NIVEL_DE_ATIVIDADE))

            if nivel_atividade == 1:
                tdee = tmb * 1.2
            elif nivel_atividade == 2:
                tdee = tmb * 1.375
            elif nivel_atividade == 3:
                tdee = tmb * 1.55
            elif nivel_atividade == 4:
                tdee = tmb * 1.725

            objetivo_selecionado = int(input(MENU_OBJETIVO_SELECIONADO))

            if objetivo_selecionado == 1:
                objetivo = 'Emagrecer'
            elif objetivo_selecionado == 2:
                objetivo = 'Manter'
            elif objetivo_selecionado == 3:
                objetivo = 'Ganhar massa'
            else:
                objetivo = 'Não definido'

            if objetivo_selecionado == 1:
                exercicio = int(input(MENU_EXERCICIO_SELECIONADO))

                calorias_objetivo = 300

                if exercicio == 1:
                    tempo_exercicio = calorias_objetivo / 5
                elif exercicio == 2:
                    tempo_exercicio = calorias_objetivo / 10
                elif exercicio == 3:
                    tempo_exercicio = calorias_objetivo / 6

            elif objetivo_selecionado == 2:
                calorias_objetivo = 200

            elif objetivo_selecionado == 3:
                exercicio = int(input(MENU_EXERCICIO_SELECIONADO))

                if exercicio == 3:
                    tempo_exercicio = 60
                else:
                    tempo_exercicio = 20

            meta_tempo_exercicios_diaria = int(input('Quantas horas diárias você quer colocar como meta? '))
            tempo_feito = int(input("Quanto tempo você treinou hoje? "))
            tempo_treino_feito = tempo_treino_feito + tempo_feito

            if meta_tempo_exercicios_diaria <= tempo_feito:
                print(f"Parabéns você concluiu sua meta diária de {meta_tempo_exercicios_diaria} horas fazendo {tempo_feito} horas ")
            else:
                print(f"Infelizmente hoje você não cumpriu sua meta de {meta_tempo_exercicios_diaria} horas, faltou {meta_tempo_exercicios_diaria - tempo_feito} horas")

        elif opcao == 7:  # Calcular para novo usuário
            possui_usuario = 'N'

        elif opcao == 8:  # Encerrar programa
            encerrar = str(input("Tem certeza que quer encerrar? [S/N]: ")).upper()
            while executar != 'S' and executar != 'N':  # valida inicio
                encerrar = str(input("Tem certeza que quer encerrar? [S/N]: ")).upper()
            if encerrar == 'S':
                executar = 'N'
                print("Programa encerrando, até a próxima...")
