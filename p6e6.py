#Yannick p6e6 Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.

numeros=[]
numeros2=[]

entrada=int(input("pasame un numero "))
entrada2=int(input(f"pasame un numero mayor que {entrada} "))


while(entrada2 < entrada):
        entrada2=int(input(f"Escribe un numero mayor que {entrada}"))    


numeros.append(entrada)
numeros.append(entrada2)

entrada3=int(input(f"Escribe un numero entre {numeros[0]} y {numeros[1]}")) 

while(entrada3 > numeros[0] and entrada3 < numeros[1]):
    numeros2.append(entrada3)
    entrada3=int(input(f"pasame un numero entre que {numeros[0]} y {numeros[1]}"))


print("Los numeros son: ", end="")
for i in range(len(numeros2)):
    print (numeros2[i], end=" ")

