#Yannick p7e6 Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.

def comprobarNombre(nombre1, caracter1):
    if (caracter1 in nombre1):
        imprimirResultado = "Si se encuentra ese carcater en el nombre"
    else:
        imprimirResultado = "No se encuentra ese caracter en el nombre"
    return imprimirResultado

nombre=input("Escribe un nombre")
caracter=input("Escribe un caracter")

print(comprobarNombre(nombre, caracter))
