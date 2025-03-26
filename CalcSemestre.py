import time
notas = []
def erro_valor():
    print("Valor inválido. Insira um valor válido...")
# -----------------------------------------------------------------------
while True: 
    print("Bem vindo ao calculo de semestre. Por favor começe colocando sua presença.")
    print("\n Digite o numero de aulas que você participou:")
    while True:
        partic_aulas = int(input())
        if 0 <= partic_aulas <= 21:
            break
        else:
            erro_valor()    
    
    p = (partic_aulas + 0.17647) * 2.833333
    presenca = round((100 * p) / 60)  
    
    if p >= (60 * 0.75):
        print(f"Parabéns! Sua presença é {presenca}% (aproximadamente {round(p, 1)} horas). Você não repetiu por faltas")
        # Inicio protocolo de presença
        for i in range(3):
            while True:
                if i == 0 or i == 1:
                    print(f"Digite a nota da P{i + 1}:")
                elif i == 2:
                    print("Digite a nota do pim:")
                
                aprende = float(input())
                if 0 <= aprende <= 10:
                    notas.append(aprende)
                    break
                else:
                    erro_valor()
        MS = (0.4 * notas[0]) + (0.4 * notas[1]) + (0.2 * notas[2])
    
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
    else:
        print("Infelizmente você ficou retido por faltas")
    # Fim protocolo de faltas.



    # fim do pograma e laço de reptição
    resposta = input("Você quer calcular a nota do proxima semestre? (sim/não)").lower().strip()
    if resposta == "sim":
        print("Certo")
        notas.clear()
    else:
        print("Tudo bem. Obrigado por usar o programa")
        break

