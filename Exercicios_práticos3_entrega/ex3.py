import random

TOTAL_DE_VOTOS = 0
TOTAL_DE_VOTOS_1 = 0
TOTAL_DE_VOTOS_2 = 0
TOTAL_DE_VOTOS_3 = 0
TOTAL_DE_VOTOS_4 = 0

TOTAL_DE_VOTOS_0 = 0
TOTAL_DE_VOTOS_9 = 0

print("As eleições vão começar, porfavor vote no seu candidato: ")
print("Digite, \"regras\", para saber como efetuar o seu voto, em caso de já saber digite, \"continuar\".")
documento = input("O que vai desejar:\t")

if documento == "regras":
    mensagem_informativa = "Para votar no seu candidato digite os números: [1];[2];[3];[4]"\
                ", cada número está associado ao respetivo candidato"\
                ", Nº1 = Candidato 1 (Fernando Mendes); Nº2 = Candidato 2"\
                " (Tino de Rans); Nº3 = Candidato 3 (Manuela Moura Guedes); Nº4 ="\
                " Candidato 4 (Zézé Camarinha). Caso não goste dos candidatos e não"\
                " queira votar digite o número 0 e vote em branco ou o digite o"\
                " número 9 e vote em nulo."
    print(mensagem_informativa) 
else:
    if documento == "continuar":     
        while True:
            lista = [-1, 0, 1, 2, 3, 4, 9]
            escolha = random.choice(lista)
            TOTAL_DE_VOTOS += 1
            if escolha == 1:
                TOTAL_DE_VOTOS_1 += 1
            elif escolha == 2:
                TOTAL_DE_VOTOS_2 += 1
            elif escolha == 3:
                TOTAL_DE_VOTOS_3 += 1
            elif escolha == 4:
                TOTAL_DE_VOTOS_4 += 1
            elif escolha == 0:
                TOTAL_DE_VOTOS_0 += 1
            elif escolha == 9:
                TOTAL_DE_VOTOS_9 += 1
            print(escolha)
            if escolha == -1:
                break
        print("No total foram feitos --> ",TOTAL_DE_VOTOS - 1,"votos")
        print("Votaram no Fernando Mendes (candidato 1):",TOTAL_DE_VOTOS_1,"pessoas")
        print("Votaram no Tino de Rans (candidato 2):",TOTAL_DE_VOTOS_2,"pessoas")
        print("Votaram na Manuela Moura Guedes (candidata 3):",TOTAL_DE_VOTOS_3,"pessoas")
        print("Votaram no Zézé Camarinha (candidato 4):",TOTAL_DE_VOTOS_4,"pessoas")

        print("Votaram em branco:",TOTAL_DE_VOTOS_0,"pessoas")
        print("Votos nulos:",TOTAL_DE_VOTOS_9)
        if TOTAL_DE_VOTOS - 1 > 0:
            calculo_candidato_1 = int(TOTAL_DE_VOTOS_1 * 100) / (TOTAL_DE_VOTOS - 1)
            calculo_candidato_2 = int(TOTAL_DE_VOTOS_2 * 100) / (TOTAL_DE_VOTOS - 1)
            calculo_candidato_3 = int(TOTAL_DE_VOTOS_3 * 100) / (TOTAL_DE_VOTOS - 1)
            calculo_candidato_4 = int(TOTAL_DE_VOTOS_4 * 100) / (TOTAL_DE_VOTOS - 1)
            calculo_candidato_0 = int(TOTAL_DE_VOTOS_0 * 100) / (TOTAL_DE_VOTOS - 1)
            calculo_candidato_9 = int(TOTAL_DE_VOTOS_9 * 100) / (TOTAL_DE_VOTOS - 1)
            print("Percetagem de votos do candidado Fernando Mendes: {0:.2f}%".format(calculo_candidato_1))
            print("Percetagem de votos do candidado Tino de Rans: {0:.2f}%".format(calculo_candidato_2))
            print("Percetagem de votos da candidada Manuela Moura Guedes: {0:.2f}%".format(calculo_candidato_3))
            print("Percetagem de votos do candidado Zézé Camatinha: {0:.2f}%".format(calculo_candidato_4))
            print("Percetagem de votos em branco: {0:.2f}%".format(calculo_candidato_0))
            print("Percetagem de votos nulos: {0:.2f}%".format(calculo_candidato_9))
        else:
            print("Não ouve votos suficiente")
