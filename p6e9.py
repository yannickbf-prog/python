#Yannick p6e9 Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
agenda = []

nombre = ""

nombre = input("Dame tu nombre")
while nombre != "S":
    contacto = []
    telefono = input("Dame el telefono")
    contacto.append(nombre)
    contacto.append(telefono)
    agenda.append(contacto)
    nombre = input("Dame tu nombre")

for i in range(len(agenda)):
    print ('\n')
    for y in range(len(agenda[i])):
        print(agenda[i][y], end=" ")
