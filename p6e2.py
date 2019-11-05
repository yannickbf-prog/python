#Yannick p6e2 Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.

numeros=[]

entrada=input("pasame un numero")
while(entrada!="salir"):
    numeros.append(int(entrada))
    entrada=input("pasame un numero")

print("la lista de numeros es ",numeros)
    

