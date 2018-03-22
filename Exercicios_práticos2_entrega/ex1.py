print("\nOlá utilizador!")
print("Porfavor introduza as suas notas dos três diferentes testes: ")

nota1 = float(input("\nTeste 1 \"25%\": "))
nota2 = float(input("Teste 1 \"35%\": "))
nota3 = float(input("Teste 1 \"40%\": "))

MAX = 20
MIN = 0

if nota1 > MAX or nota2 > MAX or nota3 > MAX:
    print("introduziu algum valor errado")
elif  nota1 < MIN or nota2 < MIN or nota3 < MIN:
        print("introduziu algum valor errado")  
elif nota1 >= MIN and nota2 >= MIN and nota3 >= MIN:
    if nota1 <= MAX and nota2 <= MAX and nota3 <= MAX:
        nota1 *= 25
        nota2 *= 35
        nota3 *= 40 
        notafinal = (nota1 + nota2 + nota3) / 100 
        print("A tua média é igual a: ",notafinal)    
        if notafinal >= 9.5:
            print("Por isso estás Aprovado")
        else:
            print("Por isso estás Reprovado")