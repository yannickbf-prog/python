#Yannick p4e2
num1=int(input("introduce un numero "))
num2=int(input("introduce un numero "))
num3=int(input("introduce un numero "))
num4=int(input("introduce un numero "))
num5=int(input("introduce un numero "))

if num1 > num2 and num2 > num3 and num3 > num4 and num4 > num5:
    print("Estan ordenados de manera decreciente")

elif num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5:
    print("Estan ordenados de manera cresciente")

else:
    print("Estan desordenados")
