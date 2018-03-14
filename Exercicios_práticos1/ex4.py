print("Introduza as suas notas: ")

nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))
nota3 = float(input("Nota3: "))

calculo1 = (nota1 * 25)
calculo2 = (nota2 * 35) 
calculo3 = (nota3 * 40) 

moduloajuda = calculo1 + calculo2 + calculo3

media = (calculo1 + calculo2 + calculo3) / 100
inteira = (calculo1 + calculo2 + calculo3) // 100
modulo = moduloajuda%100

print("A média das 3 notas é de:{0:.2f}".format(media))
print("Extras, a divisão inteira é de: {}, e o resto da divisão é de: {} ".format(int(inteira),int(modulo)))