#Yannick p5e8 Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
a=int(input("Anchura del triangulo: "))
altura=""

for i in range(a):
    print(altura)
    altura+="*"
altura="*"
for i in range(a):
    print(altura*a)
    a-=1


