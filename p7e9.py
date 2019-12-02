#Yannick p7e9 Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

def comprobarRima(palabra1, palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        resultado = f"Las palabras {palabra1} y {palabra2} riman" 
    elif palabra1[-2:] == palabra2[-2:]:
        resultado = f"Las palabras {palabra1} y {palabra2} riman un poco"   
    else:
        resultado = f"Las palabras {palabra1} y {palabra2} no riman"
    return resultado


palabraUno = input("Escribe una palabra")

palabraDos = input("Escribe otra palabra")

print(comprobarRima(palabraUno, palabraDos))
