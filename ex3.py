peso = int(input("Calcule o seu Índice de Massa Corporal, indique o seu peso em kg: "))
altura = float(input("Agora porfavor indique a sua altura em metros: "))

imc = peso / (altura ** 2) 

print("O seu IMC é de {0:.1f}".format(imc))


