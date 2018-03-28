numero = int(input("Numero: "))

for variavel in range(numero + 1, numero + 6): 
    print(variavel, end = " ")

print("\n")

for variavel1 in range(numero - 1,numero - 6, -1):
    print(variavel1, end = " ")