print("Porfavor intruduza cinco musicas do seu album, para o programa calcular a duração total no formato em hh:mm:ss" )
print("Coloque os segundos que as musica tem: ")

musica1 = int(input("primeira musica em segundos: "))
musica2 = int(input("segunda musica em segundos: "))
musica3 = int(input("terceira musica em segundos: "))
musica4 = int(input("quarta musica em segundos: "))
musica5 = int(input("quinta musica em segundos: "))

print("Coloque os minutos que as musica tem: ")

musica_1 = int(input("primeira musica em minutos: "))
musica_2 = int(input("segunda musica em minutos: "))
musica_3 = int(input("terceira musica em minutos: "))
musica_4 = int(input("quarta musica em minutos: "))
musica_5 = int(input("quinta musica em minutos: "))

calculo_segundos = (musica1 + musica2 + musica3 + musica4 + musica5)
calculo_minutos = (musica_1 + musica_2 + musica_3 + musica_4 + musica_5)
minutos_segundos = calculo_minutos * 60
unir = minutos_segundos + calculo_segundos

horas = unir // 3600
horas_e = unir % 3600
minutos = horas_e // 60
segundos = unir % 60

print("{}:{}:{}".format(horas,minutos,segundos))