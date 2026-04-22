print(f"{'=-'*10} Bem vindo ao FitCore {'=-'*10} \nA calculadora focada em seu desenvolvimento físico")
iniciar = str(input("Deseja iniciar o programa? [S/N]")).upper()

imc = 0
agua = 0
exercicio = 0
caloria_total = 0
meta = 0
tempo_treino = 0
objetivo = 0
calorias = 0
tempo = 0

while iniciar == 'S':
    dados = 'N'
    while dados == 'N':
        sexo = str(input("Qual seu sexo biologico: [M/F]")).upper()
        if sexo != 'M' and sexo != 'F':
            sexo = str(input("Algo deu errado, Digite novamente: [M/F]")).upper()
        idade = int(input("Qual a sua idade: "))
        if idade < 0 or idade > 100:
            idade = int(input("Algo deu errado, Digite novamente: "))
        peso = float(input('informe seu peso: '))
        if peso < 0 or peso > 300:
            peso = float(input("Algo deu errado, Digite novamente: "))
        altura = float(input('Agora informe a sua altura (exemplo: 1.75): '))
        if altura < 0 or altura > 3:
            altura = float(input("Algo deu errado, Digite novamente: "))
        print(f"Dados = sexo {sexo}, idade {idade}, peso {peso} e altura {altura}")
        dados = str(input("Os Dados estao corretos: [S/N]")).upper()

    encerrar = 'N'
    while encerrar == 'N':
        opcao = int(input('''Nosso programa tem varias funções, escolha qual você gostaria de calcular
[1] IMC
[2] Hidratação Diária
[3] Gasto Calórico
[4] Meta Diária
[5] Resumo diário
[6] Encerrar programa
Função escolhida: '''))

        if opcao == 1:
            imc = peso / (altura * altura)
            print(f"\nO seu imc é {imc:.2f}")
            if imc < 18.5:
                print('Você está abaixo do peso \n')
            elif imc >= 18.5 and imc < 25:
                print('Você está na média \n')
            elif imc >= 25 and imc < 30:
                print('Você está com sobrepeso \n')
            elif imc >= 30:
                print('Você está obeso \n')
            print("VOLTANDO AO MENU PRINCIPAL... \n")

        elif opcao == 2:
            agua = peso * 35
            print(f"\nPara atingir sua meta diaria de hidratação, você precisa ingerir {agua} Ml de água \n")
            print("VOLTANDO AO MENU PRINCIPAL... \n")

        elif opcao == 3:
            continuar = 'S'
            caloria_total = 0
            while continuar == 'S':
                print("""
[1] Caminhada leve
[2] Corrida
[3] Musculação
[4] Bicicleta""")
                atividade = int(input("Opção: "))

                if atividade == 1:
                    tempo = int(input('Quantos minutos? '))
                    calorias = 3.5 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    caloria_total = caloria_total + calorias
                elif atividade == 2:
                    tempo = int(input('Quantos minutos? '))
                    calorias = 8 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    caloria_total = caloria_total + calorias
                elif atividade == 3:
                    tempo = int(input('Quantos minutos? '))
                    calorias = 7 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    caloria_total = caloria_total + calorias
                elif atividade == 4:
                    tempo = int(input('Quantos minutos? '))
                    calorias = 7 * peso * (tempo / 60)
                    print(f"Você gasta {calorias:.1f} calorias")
                    caloria_total = caloria_total + calorias
                else:
                    print("Atividade inválida.")

                print(f"Total acumulado: {caloria_total:.1f}")
                continuar = input('Adicionar outra atividade? [S/N]: ').upper()

            print("VOLTANDO AO MENU PRINCIPAL...")

        elif opcao == 4:
            if sexo == "M":
                tmb = (10 * peso) + (6.25 * (altura * 100)) - (5 * idade) + 5
                print(f"Essa é a sua taxa metabólica basal: {tmb}")
            elif sexo == "F":
                tmb = (10 * peso) + (6.25 * (altura * 100)) - (5 * idade) - 161
                print(f"Essa é a sua taxa metabólica basal: {tmb}")

            nivel_atividade = int(input('''Qual nivel de atividade você ira fazer:
[1] Sedentário
[2] Levemente ativo
[3] Moderado
[4] Muito ativo
Opção escolhida:'''))

            if nivel_atividade == 1:
                tdee = tmb * 1.2
            elif nivel_atividade == 2:
                tdee = tmb * 1.375
            elif nivel_atividade == 3:
                tdee = tmb * 1.55
            elif nivel_atividade == 4:
                tdee = tmb * 1.725

            objetivo = int(input('''Qual o seu objetivo. Exemplo: 
[1] Emagrecer  
[2] Manter
[3] Ganhar massa
Objetivo: '''))

            if objetivo == 1:
                exercicio = int(input('''Qual atividade você quer praticar: 
[1] Caminhada
[2] Corrida
[3] Musculação
Opção escolhida:'''))

                if objetivo == 1:
                    calorias_objetivo = 300
                    if exercicio == 1:
                        tempo_exercicio = calorias_objetivo / 5
                    elif exercicio == 2:
                        tempo_exercicio = calorias_objetivo / 10
                    elif exercicio == 3:
                        tempo_exercicio = calorias_objetivo / 6
                elif objetivo == 2:
                    calorias_objetivo = 200
                    if exercicio == 1:
                        tempo_exercicio = calorias_objetivo / 5
                    elif exercicio == 2:
                        tempo_exercicio = calorias_objetivo / 10
                    elif exercicio == 3:
                        tempo_exercicio = calorias_objetivo / 6
                elif objetivo == 3:
                    if exercicio == 3:
                        tempo_exercicio = 60
                    else:
                        tempo_exercicio = 20

            meta = int(input('Quantas horas diárias você quer colocar como meta? '))
            tempo_feito = int(input("Quanto tempo você treinou hoje?"))
            tempo_treino = tempo + tempo_feito

            if meta <= tempo_feito:
                print(f"Parabéns você concluiu sua meta diária de {meta} horas fazendo {tempo_feito} horas ")
            else:
                print(f"Infelizmente hoje você não cumpriu sua meta de {meta} horas, faltou {meta - tempo_feito} horas")

        elif opcao == 5:
            print(f'''Vamos para seu resumo diário
O seu imc é: {imc:.2f}
Meta de hidratação: {agua}
Total de exercicios feitos: {exercicio}
Total de calorias gastas: {caloria_total}
Meta: {meta} 
tempo de treino feito: {tempo_treino}
Objetivo: {objetivo}''')
            iniciar = str(input("Gostaria de refazer os testes: [S/N]")).upper()

        elif opcao == 6:
            encerrar = str(input("Tem certeza que quer encerrar? [S/N]: ")).upper()

else:
    print("Programa encerrando, até a próxima...")