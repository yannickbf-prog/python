#Yannick p6e8 Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

limite = int(input("Escribe limite:"))

valores = int(input("Escribe un valor:"))

listavalores = []

listavalores.append(valores)

while limite > sum(listavalores):
    valores = int(input("Escribe otro valor"))
    listavalores.append(valores)
    
print(f"El limite a superar es {limite}. La lista creada es ", end="")
for i in range(len(listavalores)):
    print (listavalores[i], end=" ")
print(f"ya que la suma de estos numeros es {sum(listavalores)}")




