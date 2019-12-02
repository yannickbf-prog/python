#Yannick p7e8 Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.

def compactarFrase(frase1):
    frase1 = frase1.replace(" ", "")
    return frase1


frase = input("Escribe una frase")

print(compactarFrase(frase))
