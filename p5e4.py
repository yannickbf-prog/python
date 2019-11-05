#Yannick p5e4 Escribe un programa que pida un número y calcule su factorial.

a=int(input("Dame un numero "))
resultado=1

for i in range(1,(a+1)):
    resultado=resultado*i
        
print("El factorial de " ,a, " es: ",resultado)


