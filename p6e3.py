#Yannick p6e3 Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.

numeros=[]

entrada=float(input("pasame un numero"))
while((entrada <= 10) and (entrada >=0 )):
    numeros.append(entrada)
    entrada=float(input("pasame un numero"))

print("la lista de numeros es ",numeros)
