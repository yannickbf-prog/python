#Yannick p7e11 Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. Ésta debe devolver si es palíndroma o no , y el programa principal escribirá el resultado por pantalla:

def comprobarPalindromo(fraseONumero):

    fraseONumero = fraseONumero.replace (" ", "")

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
    print(f"{fraseONumero1} Es palindromo")
else:
    print(f"{fraseONumero1} No es palindromo")

