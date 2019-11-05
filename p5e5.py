#Yannick p5e5 Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera
a=int(input("Anchura del rectangulo: "))
b=int(input("Altura del rectangulo: "))
anchura=""

for i in range(1,(a+1)):
    anchura+="*"

for i in range(b):
        print(anchura)


    

