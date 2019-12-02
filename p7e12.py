#Yannick p7e12 Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de palabras que contiene. Debe imprimir el programa principal el resultado. Asumir que cada palabra está separada por un solo blanco:

def contarPalabras(frase):
    contadorPalabras = 1
    for i in range(0, len(frase)):
        if frase[i] == " ":
            contadorPalabras += 1
            i -= 1
            if frase[i] == " ":
                contadorPalabras -= 1
        if frase[i] == ",":
            contadorPalabras += 1
            i += 1
            if frase[i] == " ":
                contadorPalabras -= 1
        if frase[i] == ".":
            contadorPalabras += 1
            i += 1
            if frase[i] == " ":
                contadorPalabras -= 1
            #y = i+1
            #while frase[y] == " ":
                #contadorPalabras -= 1
                #y += 1

    return contadorPalabras
        

    

frase1=input("Escribe una frase")

print("La frase tiene",contarPalabras(frase1),"palabras.")


