#Yannick p3e7
fechaValidaDias=bool("false")
fechaValidaMes="false"
fechaValidaAno="false"

dia=int(input("introduce el dia "))
mes=int(input("introduce el mes "))
ano=int(input("introduce el año "))

if ano > 1900 and ano < 2021:
    fechaValidaAno="true"

if mes > 1 and mes < 12:
    fechaValidaMes="true"

if dia < 32 and dia > 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 32:
            fechaValidaDias="true"
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 31:
            fechaValidaDias="true"
    if mes == 2:
        if dia < 30:
            fechaValidaDias="true"

if fechaValidaDias == "true" and fechaValidaMes == "true" and fechaValidaAno == "true":
    print("La fecha esta bien")
else:
    print("La fecha no esta bien")
            
            
            
            
		

    



