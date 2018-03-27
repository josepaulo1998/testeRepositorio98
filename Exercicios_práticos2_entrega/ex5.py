print("\n\t\t\t\t|Conta bancária|")
print("\t\tPorfavor introduza o saldo da sua conta bancária")

while True:
    try: # caso ocorra algo errado "ValueError"(letras) este volta para o try e executa a mensagem que está no print
        saldo = float(input("\n\t\t\t\t"))
    except ValueError: # Para não deixar escrever letras
        print("\n\t\tIntroduziu um valor errado")
        continue # caso o utilizador tenha introduzio o input que eu não queria
    if saldo < 0:
        print("\n\t\tNão pode introduzir valores negativos")    
    else:
        break # Quando o utilizador introduzir tudo bem, então saiu do ciclo while

print("\n\t\tQue operação deseja realizar [debitar] ou [creditar]")
operacao = "debitar" + "creditar"
operacao_resposta = input("\n\t\t")

while True:
    if operacao_resposta not in operacao:
        print("\n\tAlgo de errado ocorreu.")
    elif operacao_resposta == "debitar":
        try:
            retirar_dinheiro = float(input("\n\t\tQuanto dinheiro pretende retirar da sua conta: "))
        except ValueError:
            print("\n\tAlgo de errado ocorreu")
            continue
        if retirar_dinheiro < 0:
            print("\n\t\tNão pode colocar números negativos, apenas coloque o valor")
        else:
            saldo_ativo1 = saldo - retirar_dinheiro
            print("\n\t\tDébito realizado com sucesso, o seu saldo é de: {}€".format(saldo_ativo1))
            break
    elif operacao_resposta == "creditar":
        try:
            acrescentar_dinheiro = float(input("\n\t\tQuanto dinheiro pretende acrescentar à sua conta bancária: ")) 
        except ValueError:
            print("\n\tAlgo de errado ocorreu")
            continue
        if acrescentar_dinheiro < 0:
            print("\n\t\tNão pode colocar números negativos, apenas coloque o valor")  
        else:
            saldo_ativo2 = saldo + acrescentar_dinheiro
            print("\n\t\tCrédito realizado com sucesso, o seu saldo é de: {}€".format(saldo_ativo2)) 
            break     