#Yannick p7e2 Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.

def mostrarApellidos(nom, ape, ape2):
    concatenarNombre = nom + " " + ape + " " + ape2
    return concatenarNombre

nombre = input("Escribe tu nombre")
apellido1 = input("Escribe tu primer apellido")
apellido2 = input("Escribe tu tercer apellido")

print(mostrarApellidos(nombre, apellido1, apellido2))

