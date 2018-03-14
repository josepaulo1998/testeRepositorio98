dados = int(input("porfavor coloque neste convertor a temperatura em Fahrenheit: "))

converter = (( dados - 32 ) * 5 ) /9.0

print("Introduziu",dados,"graus fahrenheit e o convertor passou para {0:.2f} graus centigrados".format(converter))