#Yannick p7e3 Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

def cambiarFrase(frase1):
    for i in range(len(frase1)):
        print(frase1[i])

frase = input("Escribe una frase")
cambiarFrase(frase)
