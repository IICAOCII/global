listaNombres = []
listaEdades = []

def menu():
    opcion = 1
    while(opcion!=0):
        print("1. pedir datos")
        print("2. Imprimir datos")
        print("3. generar pdf")
        print("4. generar QR")
        print("0. Salir")
        opcion = int(input("elije una opcionn"))
        if(opcion==1):
           pedirDatos()
        elif(opcion==2):
           imprimirDatos()

def pedirDatos():
    listaNombres.append(input("ingresa un nombre"))
    listaEdades.append(input("ingresa una edad "))
    print("guardado")
def imprimirDatos():
    for i in range(len(listaNombres)):
        print(f"Nombre: {listaNombres[i]} Edad: {listaEdades[i]}")