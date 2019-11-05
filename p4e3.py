#Yannick p4e3
trianguloOCuadrado=input("introduce triangulo o cuadrado ")
areaTriangulo=0

if trianguloOCuadrado=="triangulo":
    alturaTriangulo=int(input("introduce la altura del triangulo"))
    baseTriangulo=int(input("introduce la base del triangulo"))
    areaTriangulo=alturaTriangulo * baseTriangulo / 2
    print("La area del triangulo es de" , areaTriangulo)

