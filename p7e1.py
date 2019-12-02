#Yannick p7e1 Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

def cambiarTexto(txt):
    print (txt.upper())
    print (txt.lower())

texto = input("Escribe un texto")
cambiarTexto(texto)


