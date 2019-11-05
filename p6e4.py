#Yannick p6e4 Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.

numeros=[]

entrada=int(input("pasame un numero"))
entrada2=int(input(f"pasame un numero mayor que {entrada}"))

while(entrada >= entrada2):
    entrada2=int(input(f"{entrada2} no es mayor que {entrada}. Vuelve a introducir un numero"))

numeros.append(entrada)
numeros.append(entrada2)
print(f"la lista de numeros es {numeros}")
