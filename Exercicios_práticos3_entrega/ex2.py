print("Apresente um número inteiro:")
numero = int(input("\n"))

if numero > 1:
    for variavel in range(2,numero):
        if numero % variavel == 0:
            print(numero,"<- Não é um número primo")
            break
    else:
        print(numero,"<- É um número primo")        
else: # se for menor ou igual a um, não é primo
    print(numero,"<- Não é um número primo")        