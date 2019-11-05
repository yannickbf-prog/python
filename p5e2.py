#Yannick p5e2

a=int(input("Escribe un numero "))
b=int(input("Escribe un numero mayor que %s "%(a)))

if (a < b):    
    for i in range(a,(b+1)):
        if i%2 == 0:
            print("El numero " ,i, " es par")
        else:
            print("El numero ",i, "es impar")
        


