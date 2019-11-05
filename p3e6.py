#Yannick p3e6

a=int(input("introduce el precio del producto"))
b=input("introduce el nombre del producto")

precioConIva=a*21/100 + a

print("Tu " + b + " vale " , a , " euros y con el 21 % de IVA se queda en " , precioConIva , " euros en total")
