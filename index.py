import time

# Funções:
nota_semestre_1 = []  # aqui armazena as notas do semestre 1
nota_semestre_2 = []  # e aqui armazena as notas do semestre 2

def semestre(num_semestre):
    if num_semestre == 1:
        print("Digite o numero de aulas que você participou no primeiro semestre:")
        notas_semestre = nota_semestre_1  # semestre 1
    elif num_semestre == 2:
        print("Digite o numero de aulas que você participou no segundo semestre:")
        notas_semestre = nota_semestre_2  # semestre 2
    
    while True:
        partic_aulas = int(input())
        if 0 <= partic_aulas <= 21:
            break
        else:
            erro_valor()    
    
    p = (partic_aulas + 0.17647) * 2.833333
    presenca = round((100 * p) / 60)  # Arredondando a presença
    
    if p >= (60 * 0.75):
        print(f"Parabéns! Sua presença é {presenca}% (aproximadamente {round(p, 1)} horas). Você não repetiu por faltas")
    else:
        print("Infelizmente você ficou retido por faltas")
        return
    
    print("Caso você não tenha feito uma das provas, basta colocar a nota da substitutiva.")
    time.sleep(2)
    
    for i in range(3):
        while True:
            if i == 0 or i == 1:
                print(f"Digite a nota da P{i + 1}:")
            elif i == 2:
                print("Digite a nota do pim:")
                
            aprende = float(input())
            if 0 <= aprende <= 10:
                notas_semestre.append(aprende)
                break
            else:
                erro_valor()
    
    MS = (0.4 * notas_semestre[0]) + (0.4 * notas_semestre[1]) + (0.2 * notas_semestre[2])
    
    if MS >= 7:
        print(f"Parabéns. Você passou no semestre {num_semestre}")
    else:
        print(f"Infelizmente você teve que fazer exame no semestre {num_semestre}.")
        while True:
            exame = float(input("Digite a nota do exame: "))
            if 0 <= exame <= 10:
                break
            else:
                erro_valor()
        
        MF = (MS + exame) / 2
        if MF >= 5:
            print(f"Parabéns. Você passou no semestre {num_semestre}")
        else:
            print(f"Infelizmente você ficou retido no semestre {num_semestre}")

def erro_valor():
    print("Valor inválido. Insira um valor válido...")

def ano():
    print(f"Notas do semestre 1: {nota_semestre_1}")
    print(f"Notas do semestre 2: {nota_semestre_2}")
    
    if len(nota_semestre_1) > 0 and len(nota_semestre_2) > 0:
        media_ano = (sum(nota_semestre_1) + sum(nota_semestre_2)) / (len(nota_semestre_1) + len(nota_semestre_2))
        print(f"A média do ano (considerando os dois semestres) é: {media_ano}")
    else:
        print("Nenhuma nota registrada para um dos semestres.")

# Loop para sair
while True:
    escolha_op_s = input("Você quer saber se passou em uma matéria no semestre ou no curso? (semestre/ano/sair): ").lower().strip()

    if escolha_op_s == "semestre":
        semestre(1)  # Chama a função para o primeiro semestre
        semestre(2)  # Chama a função para o segundo semestre
    elif escolha_op_s == "ano":
        ano()  # Mostra as notas e a média dos dois semestres
    elif escolha_op_s == "sair":
        print("Programa encerrado.")
        break  # Sai do loop e termina o programa
    else:
        print("Valor incorreto")
