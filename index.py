import time

# Funções:
nota = []

def semestre():
    print("Digite o numero de aulas que você participou:")
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
                nota.append(aprende)
                break
            else:
                erro_valor()
    
    MS = (0.4 * nota[0]) + (0.4 * nota[1]) + (0.2 * nota[2])
    
    if MS >= 7:
        print("Parabéns. Você passou no semestre")
    else:
        print("Infelizmente você teve que fazer exame.")
        while True:
            exame = float(input("Digite a nota do exame: "))
            if 0 <= exame <= 10:
                break
            else:
                erro_valor()
        
        MF = (MS + exame) / 2
        if MF >= 5:
            print("Parabéns. Você passou no semestre")
        else:
            print("Infelizmente você ficou retido")

def erro_valor():
    print("Valor inválido. Insira um valor válido...")

def ano():
    print(f"Notas no ano: {nota}")

# Chamada da função:
escolha_op_s = input("Você quer saber se passou em uma matéria no semestre ou no curso? (semestre/ano): ").lower().strip()

if escolha_op_s == "semestre":
    semestre()
elif escolha_op_s == "ano":
    ano()
else:
    print("Valor incorreto")
