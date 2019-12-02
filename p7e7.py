#Yannick p7e9 Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

def contarVocales(frase1):
    contadorVocales = 0
    vocales = ["a", "e", "i", "o", "u"]
    for i in range(0, len(frase1)):
        if frase1[i] in vocales:
            contadorVocales += 1
    return contadorVocales

frase = input("Escribe una frase")

print(contarVocales(frase))
