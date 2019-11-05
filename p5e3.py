#Yannick p5e3 Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último

a=int(input("Escribe un numero "))
b=int(input("Escribe un numero mayor que %s "%(a)))
resultado=0

if (a < b):
    for i in range((a+1),b):        
        #print(i)
        #resultado=resultado+i
        resultado+=i
        
    resultado=resultado + a + b
    print("La suma desde " , a ," hasta " ,b, " es " , resultado)

