#Yannick p7e10 Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:

def comprobarPalindromo(fraseONumero):

    contarFraseONumero = int(len(fraseONumero) / 2)

    #print(fraseONumero)

    y = 1
    esPalindromo = True
    for i in range(0, (contarFraseONumero)):
        

        #print(fraseONumero[i])
        #print(fraseONumero[-y])
        if (fraseONumero[i]) != (fraseONumero[-y]):
            esPalindromo = False    
        #guardarPalabraInversa = guardarPalabraInversa +(fraseONumero[i])
        y = y+1
    return esPalindromo

fraseONumero1=input("Escribe una frase o numero")
if (comprobarPalindromo(fraseONumero1)):
    print("Es palindromo")
else:
    print("No es palindromo")

