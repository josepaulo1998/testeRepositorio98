def teste(numero,letra):
    for i in range(numero,0,-1):
        if i == 0:
            continue
        print(i * letra)
def ola():
    numero = int(input("numero:"))
    letra = input("letra:")
    teste(numero,letra)

ola()
