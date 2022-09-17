i = 100

print("**MENÚ**")
print("0.SALUDAR")
print("1.DE3SPEDIR")
print("2.SALIR")

while(i != 0):
    i = int(input("Ingrese una opcion: "))
    if(i == 0):
        print("Hola")
    elif(i == 1):
        print("Chaoo")
    elif(i == 2):
        break
