print("Escreva dois numeros porfavor:\n")

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print("O numero: {}, é maior que o numero {} ".format(num1,num2))
else:
    print("O numero: {}, é maior que o numero {} ".format(num2,num1))