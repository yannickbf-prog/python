#Yannick p6e7 Escribe un programa que pida un número (límite) y luego te pida
#números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.

limite = int(input("Escribe el limite"))

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

