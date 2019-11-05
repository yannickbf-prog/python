#Yannick p5e9 Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:

a=int(input("Anchura del triangulo: "))
b=int(input("Altura del triangulo "))

asterisco="*"
espacio=" "
espacio=espacio*(a-4)

print(asterisco*a)

for i in range(b-2):
    print(asterisco , espacio , asterisco)

print(asterisco*a)
