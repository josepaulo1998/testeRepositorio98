print("\nOlá utilizador!")
print("Porfavor introduza as suas notas dos três diferentes testes: ")

nota1 = float(input("\nTeste 1 \"25%\": "))
nota2 = float(input("Teste 1 \"35%\": "))
nota3 = float(input("Teste 1 \"40%\": "))

nota1 *= 25
nota2 *= 35
nota3 *= 40 

notafinal = (nota1 + nota2 + nota3) / 100

if nota1 or nota2 or nota3 > 20:
    print("Colocou algo de errado nas suas notas!")
elif nota1 or nota2 or nota3 < 0:
    print("Colocou algo de errado nas suas notas!")
elif notafinal >= 9.5:
    print("Aprovado")
else:
    print("Reprovado")
    
    