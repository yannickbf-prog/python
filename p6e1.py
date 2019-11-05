#Yannick p6e1 Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.

palabras=[]

entrada=input("pasame una palabra")
while(entrada!=""):
    palabras.append(entrada)
    entrada=input("pasame una palabra")

print("la lista de palabras es ",palabras)
    
