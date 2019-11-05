#Yannick p5e10 Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:

a=int(input("Altura del triangulo "))

asterisco = "*"
espacio = " "

for i in range(a):
    espacio = " "
    espacio = espacio * a
    print(espacio, asterisco, espacio)
    a-=1
    asterisco += "**"
    
    
    
