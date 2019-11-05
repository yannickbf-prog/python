#Yannick p5e11 Escribe un programa que pida un número e imprima todos sus divisores.

a=int(input("Dame un numero "))
b=1
guardar_resultado=""

for i in range(a):
    resultado=a%b
    if resultado == 0:
        guardar_resultado+= "%s "%(b)
    b+=1
print("Los divisores de %s son:"%(a),guardar_resultado)

    

