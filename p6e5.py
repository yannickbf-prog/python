#Yannick p6e5 Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.

numeros=[]

entrada=int(input("pasame un numero "))
entrada2=int(input(f"pasame un numero mayor que {entrada} "))

if(entrada < entrada2):
    numeros.append(entrada)
    numeros.append(entrada2)

while(numeros[-2] <= numeros[-1]):
    entrada3=int(input(f"pasame un numero mayor que {numeros[-1]} "))
    numeros.append(entrada3)

print("Los numeros son: ", end="")
for i in range(len(numeros)):
    print (numeros[i], end=" ")

