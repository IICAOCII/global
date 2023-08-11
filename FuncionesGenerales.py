from FuncionesPDF import * 
from reportlab.pdfgen import canvas
from FuncionesPDF import generarPDF
from DatosEstaticos import (listaBebidasgrandes, listaBebidasPequeñas, lista_Precios_BebidasGrandes,
    lista_Precios_BebidasPequeñas, listaComplementos, listaRecetas,
    obtener_lista_ingredientes, obtener_lista_Tamanos, lista_Precios_Tamanos,
    generar_codigo_rastreo,listacombos,random)

listaNombres = []
listaCorreos = []
listaDirecciones = []
listaPizzasPersonalizadas = []
listaRecetasElegidas = []
listaTamanos = []
listaPrecios = []
listaBebidasElegidas = []
listaComplementosElegidos = []
listaIngredientesElegidos = []
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

def Personalizada(tipo_pedido):
    precio_complemento = 70  
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    correo_cliente = input("Ingrese el correo electrónico del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")

    listaNombres.append(nombre_cliente)
    listaCorreos.append(correo_cliente)
    listaDirecciones.append(direccion_cliente)
    listaBebidasElegidas.append([])
    listaComplementosElegidos.append([])
    listaIngredientesElegidos.append([])

    print("Lista de ingredientes (escoje tres para armar tu pizza personalizada):")
    mostrarIngredientes()

    mostrarIngredientes()
    ingredientes_elegidos = []
    for _ in range(3):
        opcion = int(input("Elija un ingrediente (1-30): "))
        if 1 <= opcion <= 30:
            ingrediente_elegido = obtener_lista_ingredientes()[opcion - 1]
            ingredientes_elegidos.append(ingrediente_elegido)
        else:
            print("Opción inválida. Intente de nuevo.")

    listaIngredientesElegidos.append(ingredientes_elegidos)

    
    
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


    
def recetas(tipo_pedido):
    precio_complemento = 70  
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    correo_cliente = input("Ingrese el correo electrónico del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")

    listaNombres.append(nombre_cliente)
    listaCorreos.append(correo_cliente)
    listaDirecciones.append(direccion_cliente)
    listaBebidasElegidas.append([])
    listaComplementosElegidos.append([])

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
    

def imprimirDetallesPedido(tipo_pedido):
    if not listaNombres:
        print("No hay usuarios registrados.")
        return

    print("Clientes registrados:")
    for i, nombre in enumerate(listaNombres, 1):
        print(f"{i}. {nombre}")

    try:
        numero_usuario = int(input("Ingrese el número de usuario para ver los detalles del pedido: ")) - 1
        if 0 <= numero_usuario < len(listaNombres):
            print("\nDatos del usuario:")
            print(f"Nombre: {listaNombres[numero_usuario]}")
            print(f"Correo: {listaCorreos[numero_usuario]}")
            print(f"Dirección: {listaDirecciones[numero_usuario]}")

            tipo_pedido_usuario = tipo_pedido[numero_usuario]
            if tipo_pedido_usuario == "personalizada":
                print("Elecciones de", listaNombres[numero_usuario])
                print("Ingredientes elegidos:", ", ".join(listaPizzasPersonalizadas[numero_usuario]))
                print("Tamaño elegido:", listaTamanos[numero_usuario])
                print("Precio:", listaPrecios[numero_usuario])
            elif tipo_pedido_usuario == "recetas":
                print("Receta elegida:", listaRecetasElegidas[numero_usuario])
                print("Tamaño elegido:", listaTamanos[numero_usuario])
                print("Precio:", listaPrecios[numero_usuario])

            if listaBebidasElegidas[numero_usuario]:
                print("\nBebidas elegidas:")
                for bebida, cantidad, precio_total in listaBebidasElegidas[numero_usuario]:
                    print(f"{bebida} - Cantidad: {cantidad} - Precio: {precio_total}")

            if listaComplementosElegidos[numero_usuario]:
                print("\nComplementos elegidos:")
                for complemento, cantidad, precio_total in listaComplementosElegidos[numero_usuario]:
                    print(f"{complemento} - Cantidad: {cantidad} - Precio: {precio_total}")

        else:
            print("Número de usuario inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")




def imprimir_datos_usuario(numero_usuario):
    if 1 <= numero_usuario <= len(listaNombres):
        nombre = listaNombres[numero_usuario - 1]
        correo = listaCorreos[numero_usuario - 1]
        direccion = listaDirecciones[numero_usuario - 1]
        tipo_pedido_usuario = tipo_pedido[numero_usuario -1]

      
        print("\nDatos del usuario:")
        print(f"Nombre: {nombre}")
        print(f"Correo: {correo}")
        print(f"Dirección: {direccion}")

        if tipo_pedido_usuario == "personalizada":
            ingredientes = listaPizzasPersonalizadas[numero_usuario - 1]
            print("Ingredientes elegidos:", ", ".join(ingredientes))
        elif tipo_pedido == "recetas":
            receta = listaRecetasElegidas[numero_usuario - 1]
            print("Receta elegida:", receta)

        if listaBebidasElegidas[numero_usuario - 1]:
            print("Bebidas elegidas:")
            for bebida, cantidad, precio_total in listaBebidasElegidas[numero_usuario -1]:
                print(f"{bebida} - Cantidad: {cantidad} - Precio: {precio_total}")

        if listaComplementosElegidos[numero_usuario - 1]:
            print("Complementos elegidos:")
            for complemento, cantidad, precio_total in listaComplementosElegidos[numero_usuario - 1]:
                print(f"{complemento} - Cantidad: {cantidad} - Precio: {precio_total}")
    else:
        print("Número de usuario inválido.")



def imprimirDatos():
    for i, nombre in enumerate(listaNombres, 1):
         print(f"{i}. {nombre} - NoCl: {generar_codigo_rastreo()}")


def combos():
   listacombos()

def generar_codigo_rastreo():
    return str(random.randint(1000000, 9999999))

no_pedido = generar_codigo_rastreo()



def menuPedido():
    c = canvas.Canvas("nombre_del_archivo.pdf")  
    opcion = 1
    while opcion != 0:
        print("1. Pizza sencilla 3 ingredientes")
        print("2. Menú pizzas (recetas)")
        print("3. Combos")
        print("4. lista clientes ")
        print("5. imprimir detalles de pedido por cliente")
        print("6. generar pdf cliente ")
        print("0. Salir")
        opcion = int(input("Elije una opción: "))
        if opcion == 1:
           tipo_pedido = "personalizada"
           Personalizada(tipo_pedido)
        elif opcion == 2:
           tipo_pedido = "receta"
           recetas(tipo_pedido)
        elif opcion == 3:
            combos()
        elif opcion == 4:
            imprimirDatos()
        elif opcion ==5:
            imprimirDetallesPedido(tipo_pedido)
        elif opcion == 6:
             numero_cliente = int(input("Elije el número de cliente para generar el PDF: ")) - 1
             if 0 <= numero_cliente < len(listaNombres):
                datos_cliente = {
                    'nombre': listaNombres[numero_cliente],
                    'direccion': listaDirecciones[numero_cliente],
                    'correo': listaCorreos[numero_cliente]
                }

                tipo_pedido_cliente = tipo_pedido[numero_cliente]
                datos_pedido_cliente = {
                    'ingredientes': listaPizzasPersonalizadas[numero_cliente],
                    'tamano': listaTamanos[numero_cliente],
                    'bebidas': listaBebidasElegidas[numero_cliente],
                    'complementos': listaComplementosElegidos[numero_cliente]
                } if tipo_pedido_cliente == "personalizada" else {
                    'receta': listaRecetasElegidas[numero_cliente],
                    'tamano': listaTamanos[numero_cliente],
                    'bebidas': listaBebidasElegidas[numero_cliente],
                    'complementos': listaComplementosElegidos[numero_cliente]
                }

                generarPDF(c, ruta, nombreQR, datos_cliente, tipo_pedido_cliente, datos_pedido_cliente)
        c.save()