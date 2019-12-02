#Yannick p7e4 Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. La función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el resultado para que el programa principal la imprima por pantalla

def nuevaFrase(frase1):
    
    frase1 = frase1.replace(" ", "*")
    print(frase1)
    

frase = input("Escribe una frase ")
nuevaFrase(frase)

