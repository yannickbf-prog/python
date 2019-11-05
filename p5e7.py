#Yannick p5e7 Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
a=int(input("Altura del triangulo: "))
altura="*"

for i in range(a):
    print(altura*a)
    a-=1

