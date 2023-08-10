from FuncionesPDF import * 

from DatosEstaticos import *

listaNombres = []
listaCorreos = []
listaDirecciones = []
listaPizzasPersonalizadas = []
listaRecetasElegidas = []
listaTamanos = []
listaPrecios = []
listaBebidasElegidas = []
listaComplementosElegidos = []
tipo_pedido = None

lista_Precios_Tamanos = [
    200,
    275,
    305,
    329,
    305,
    375
]


def mostrarIngredientes():
    lista_ingredientes = obtener_lista_ingredientes()

    for i, ingrediente in enumerate(lista_ingredientes, 1):
        print(f"{i}. {ingrediente}")

def Personalizada():
    precio_complemento = 70  
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    correo_cliente = input("Ingrese el correo electrónico del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")

    listaNombres.append(nombre_cliente)
    listaCorreos.append(correo_cliente)
    listaDirecciones.append(direccion_cliente)

    print("Lista de ingredientes (escoje tres para armar tu pizza personalizada):")
    mostrarIngredientes()

    ingredientes_elegidos = []
    for _ in range(3):
        opcion = int(input("Elija un ingrediente (1-30): "))
        if 1 <= opcion <= 30:
            ingrediente_elegido = obtener_lista_ingredientes()[opcion - 1]
            ingredientes_elegidos.append(ingrediente_elegido)
        else:
            print("Opción inválida. Intente de nuevo.")

    listaPizzasPersonalizadas.append(ingredientes_elegidos)
    
    print("\nLista de tamaños disponibles:")
    for i, tamano in enumerate(obtener_lista_Tamanos(), 1):
        precio = lista_Precios_Tamanos[i - 1]
        print(f"{i}. {tamano} - Precio: {precio}")

    opcion_tamano = int(input("Elija un tamaño (1-6): "))
    if 1 <= opcion_tamano <= 6:
        tamano_elegido = obtener_lista_Tamanos()[opcion_tamano - 1]
        precio_elegido = lista_Precios_Tamanos[opcion_tamano - 1]
    else:
        print("Opción inválida. Seleccionando tamaño por defecto.")
        tamano_elegido = obtener_lista_Tamanos()[0]
        precio_elegido = lista_Precios_Tamanos[0]
    listaTamanos.append(tamano_elegido)
    listaPrecios.append(precio_elegido)


    print("\nElecciones de", nombre_cliente)
    print("Ingredientes elegidos:", ", ".join(ingredientes_elegidos))
    print("Tamaño elegido:", tamano_elegido)
    print("Precio:", precio_elegido)

    bebidas_elegidas = []
    cantidades_bebidas = []
    complementos_elegidos = []
    cantidades_complementos = []


    agregar_mas = input("¿Desea agregar complementos o bebidas? (si/no): ").lower()
    while agregar_mas == "si":
        print("\nOpciones disponibles:")
        print("1. Bebidas")
        print("2. Complementos")
        opcion_agregar = int(input("Elija una opción (1-2): "))

        if opcion_agregar == 1:
            print("\nLista de bebidas grandes:")
            for i, bebida in enumerate(listaBebidasgrandes, 1):
                precio = lista_Precios_BebidasGrandes[i - 1]
                print(f"{i}. {bebida} - Precio: {precio}")

            print("\nLista de bebidas pequeñas:")
            for i, bebida in enumerate(listaBebidasPequeñas, 1):
                precio = lista_Precios_BebidasPequeñas[i - 1]
                print(f"{i + 10}. {bebida} - Precio: {precio}")

            opcion_bebida = int(input("Elija una bebida (1-20): "))
            if 1 <= opcion_bebida <= 20:
                bebida_elegida = listaBebidasgrandes[opcion_bebida - 1] if opcion_bebida <= 10 else listaBebidasPequeñas[opcion_bebida - 11]
                cantidad_bebida = int(input("Elija la cantidad que desea: "))
                precio_bebida = lista_Precios_BebidasGrandes[opcion_bebida - 1] if opcion_bebida <= 10 else lista_Precios_BebidasPequeñas[opcion_bebida - 11]
                bebidas_elegidas.append([bebida_elegida, cantidad_bebida, precio_bebida * cantidad_bebida])
                cantidades_bebidas.append(cantidad_bebida)
                

            else:
                print("Opción inválida.")

        elif opcion_agregar == 2:
            print("\nLista de complementos:")
            for i, complemento in enumerate(listaComplementos(), 1):
                precio = 70
                print(f"{i}. {complemento} - Precio: {precio}")

            opcion_complemento = int(input("Elija un complemento (1-20): "))
            if 1 <= opcion_complemento <= 20:
                complemento_elegido = listaComplementos()[opcion_complemento - 1]
                cantidad_complemento = int(input("Elija la cantidad que desea: "))
                precio_complemento =70
                complementos_elegidos.append([complemento_elegido, cantidad_complemento, precio_complemento * cantidad_complemento])
                cantidades_complementos.append(cantidad_complemento)

            else:
                print("Opción inválida.")

        else:
            print("Opción inválida.")

        agregar_mas = input("¿Desea agregar algo más? (si/no): ").lower()

    print("\nElecciones de", nombre_cliente)
    print("Ingredientes elegidos:", ", ".join(ingredientes_elegidos))
    print("Tamaño elegido:", tamano_elegido)
    print("Precio:", precio_elegido)

    if bebidas_elegidas:
        print("\nBebidas elegidas:")
        for bebida, cantidad in zip(bebidas_elegidas, cantidades_bebidas):
            precio_bebida = 70
            print(f"{bebida} - Cantidad: {cantidad} - Precio: {precio_bebida * cantidad}")

    if complementos_elegidos:
        print("\nComplementos elegidos:")
        for complemento, cantidad in zip(complementos_elegidos, cantidades_complementos):
            print(f"{complemento} - Cantidad: {cantidad} - Precio: {precio_complemento * cantidad}")

    print("Guardado")
    print("pedido generado con exito para cliente", nombre_cliente)
    tipo_pedido = "Personalizada"

    
def recetas():
    precio_complemento = 70  
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    correo_cliente = input("Ingrese el correo electrónico del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")

    listaNombres.append(nombre_cliente)
    listaCorreos.append(correo_cliente)
    listaDirecciones.append(direccion_cliente)

    print("Lista de recetas disponibles:")
    for i, receta in enumerate(listaRecetas(), 1):
        print(f"{i}. {receta}")

    receta_elegida = None
    while receta_elegida is None:
        opcion_receta = int(input("Elija una receta (1-30): "))
        if 1 <= opcion_receta <= 30:
            receta_elegida = listaRecetas()[opcion_receta - 1]
        else:
            print("Opción inválida. Intente de nuevo.")
    
    listaRecetasElegidas.append(receta_elegida)


    print("\nLista de tamaños disponibles:")
    for i, tamano in enumerate(obtener_lista_Tamanos(), 1):
        precio = lista_Precios_Tamanos[i - 1]
        print(f"{i}. {tamano} - Precio: {precio}")

    opcion_tamano = int(input("Elija un tamaño (1-6): "))
    if 1 <= opcion_tamano <= 6:
        tamano_elegido = obtener_lista_Tamanos()[opcion_tamano - 1]
        precio_elegido = lista_Precios_Tamanos[opcion_tamano - 1]
    else:
        print("Opción inválida. Seleccionando tamaño por defecto.")
        tamano_elegido = obtener_lista_Tamanos()[0]
        precio_elegido = lista_Precios_Tamanos[0]
    listaTamanos.append(tamano_elegido)
    listaPrecios.append(precio_elegido)

    print("\nElecciones de", nombre_cliente)
    print("Receta elegida:", receta_elegida)
    print("Tamaño elegido:", tamano_elegido)
    print("Precio:", precio_elegido)

    bebidas_elegidas = []
    cantidades_bebidas = []
    complementos_elegidos = []
    cantidades_complementos = []


    agregar_mas = input("¿Desea agregar complementos o bebidas? (si/no): ").lower()
    while agregar_mas == "si":
        print("\nOpciones disponibles:")
        print("1. Bebidas")
        print("2. Complementos")
        opcion_agregar = int(input("Elija una opción (1-2): "))

        if opcion_agregar == 1:
            print("\nLista de bebidas grandes:")
            for i, bebida in enumerate(listaBebidasgrandes, 1):
                precio = lista_Precios_BebidasGrandes[i - 1]
                print(f"{i}. {bebida} - Precio: {precio}")

            print("\nLista de bebidas pequeñas:")
            for i, bebida in enumerate(listaBebidasPequeñas, 1):
                precio = lista_Precios_BebidasPequeñas[i - 1]
                print(f"{i + 10}. {bebida} - Precio: {precio}")

            opcion_bebida = int(input("Elija una bebida (1-20): "))
            if 1 <= opcion_bebida <= 20:
                bebida_elegida = listaBebidasgrandes[opcion_bebida - 1] if opcion_bebida <= 10 else listaBebidasPequeñas[opcion_bebida - 11]
                cantidad_bebida = int(input("Elija la cantidad que desea: "))
                precio_bebida = lista_Precios_BebidasGrandes[opcion_bebida - 1] if opcion_bebida <= 10 else lista_Precios_BebidasPequeñas[opcion_bebida - 11]
                bebidas_elegidas.append([bebida_elegida, cantidad_bebida, precio_bebida * cantidad_bebida])
                cantidades_bebidas.append(cantidad_bebida)
            else:
                print("Opción inválida.")

        elif opcion_agregar == 2:
            print("\nLista de complementos:")
            for i, complemento in enumerate(listaComplementos(), 1):
                precio = 70
                print(f"{i}. {complemento} - Precio: {precio}")

            opcion_complemento = int(input("Elija un complemento (1-20): "))
            if 1 <= opcion_complemento <= 20:
                complemento_elegido = listaComplementos()[opcion_complemento - 1]
                cantidad_complemento = int(input("Elija la cantidad que desea: "))
                precio_complemento = 70
                complementos_elegidos.append([complemento_elegido, cantidad_complemento, precio_complemento * cantidad_complemento])
                cantidades_complementos.append(cantidad_complemento)
            else:
                print("Opción inválida.")

        else:
            print("Opción inválida.")

        agregar_mas = input("¿Desea agregar algo más? (si/no): ").lower()

    print("\nElecciones de", nombre_cliente)
    print("Receta elegida:", receta_elegida)
    print("Tamaño elegido:", tamano_elegido)
    print("Precio:", precio_elegido)
    
    if bebidas_elegidas:
        print("\nBebidas elegidas:")
        for bebida, cantidad in zip(bebidas_elegidas, cantidades_bebidas):
            precio_bebida = 70
            print(f"{bebida} - Cantidad: {cantidad} - Precio: {precio_bebida * cantidad}")

    if complementos_elegidos:
        print("\nComplementos elegidos:")
        for complemento, cantidad in zip(complementos_elegidos, cantidades_complementos):
            precio_complemento = 70
            print(f"{complemento} - Cantidad: {cantidad} - Precio: {precio_complemento * cantidad}")

    print("Guardado")
    print("Pedido registrado con éxito para", nombre_cliente)
    tipo_pedido = "receta"

def imprimirPedido(nombre_cliente):
    if nombre_cliente in listaNombres:
        indice_cliente = listaNombres.index(nombre_cliente)
        print("\ndetalles del pedido de", nombre_cliente)
        print("correo electronico: ", listaDirecciones[indice_cliente])
        print("Direccion: ",listaDirecciones[indice_cliente])
    
    if tipo_pedido == "personalizada":
        print("\nDetalles de la pizza personalizada: ")
        print("<Ingredientes elegidos:",",".join(listaPizzasPersonalizadas[indice_cliente]))
        print("Tamaño elegido:",listaTamanos[indice_cliente])
        print("precio:",listaPrecios[indice_cliente])
    
    elif tipo_pedido == "receta":
        print("\ndetalles de la receta:")
        print("Receta elegida:",listaRecetasElegidas[indice_cliente])
        print("Tamaño elegido:",listaTamanos[indice_cliente])
        print("precio:",listaPrecios[indice_cliente])

    if indice_cliente < len(listaBebidasElegidas):
            print("\nBebidas elegidas:")
            for bebida_info in listaBebidasElegidas[indice_cliente]:
                bebida, cantidad, precio_total = bebida_info
                print(bebida, "- Cantidad:", cantidad, "- Precio:", precio_total)

        # Imprimir complementos elegidos
    if indice_cliente < len(listaComplementosElegidos):
            print("\nComplementos elegidos:")
            for complemento_info in listaComplementosElegidos[indice_cliente]:
                complemento, cantidad, precio_total = complemento_info
                print(complemento, "- Cantidad:", cantidad, "- Precio:", precio_total)
    else:
        print("\nEl cliente no se encuentra en la lista de nombres.")





def imprimirDatos():
    for i, nombre in enumerate(listaNombres, 1):
         print(f"{i}. {nombre} - NoCl: {generar_codigo_rastreo()}")

def imprimirDetallesPedido():
    if not listaNombres:
        print("No hay clientes registrados en la lista.")
        return

    imprimirDatos()
    opcion_cliente = int(input("Elija el número de cliente para ver los detalles del pedido: "))
    if 1 <= opcion_cliente <= len(listaNombres):
        nombre_cliente = listaNombres[opcion_cliente - 1]
        imprimirPedido(nombre_cliente)
    else:
        print("Opción inválida.")


def combos():
    listacombos()

def generar_codigo_rastreo():
    return str(random.randint(1000000, 9999999))

no_pedido = generar_codigo_rastreo()



def menuPedido():
    opcion = 1
    while opcion != 0:
        print("1. Pizza sencilla 3 ingredientes")
        print("2. Menú pizzas (recetas)")
        print("3. Combos")
        print("4. lista clientes ")
        print("5. imprimir detalles de pedido por cliente")
        print("0. Salir")
        opcion = int(input("Elije una opción: "))
        if opcion == 1:
           Personalizada()
        elif opcion == 2:
           recetas()
        elif opcion == 3:
            combos()
        elif opcion == 4:
            imprimirDatos()
        elif opcion ==5:
            imprimirDetallesPedido()
        elif opcion == 10:
            generarPDF(listaNombres)
