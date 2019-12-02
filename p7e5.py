#Yannick p7e5 Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá:

def modificarFrase(frase1, vocal1):

    frase1 = frase1.replace("a", vocal1)
    frase1 = frase1.replace("e", vocal1)
    frase1 = frase1.replace("1", vocal1)
    frase1 = frase1.replace("o", vocal1)
    frase1 = frase1.replace("u", vocal1)
    return frase1

frase = input("Dime algo")
vocal = input("Dime una vocal ")
print(modificarFrase(frase, vocal))

