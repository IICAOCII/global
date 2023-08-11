from reportlab.pdfgen import canvas
from FuncionesQR import *
from FuncionesGenerales import *
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
ruta = "C:/Users/Lenovo/Desktop/prueba funciones/prubea funciones/"
nombreQR = ruta + "miQR.png"

def generarPDF(c, ruta, nombreQR, datos_cliente, tipo_pedido, datos_pedido):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + "reporteGlobal_"+fecha_actual.strftime('%d_%m_%y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "hola desde funcion")
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    c.setFont('Helvetica',20)
    c.setFont('Helvetica-Bold', 18)
    c.drawString(210, 740, "Datos del Cliente ")
    c.setFont('Helvetica', 14)
    c.drawString(70,720,"-------------------------------------------------------------------------------------------")
    c.drawString(50, 700, "NOMBRE: ")
    c.drawString(400, 700, f" {datos_cliente['nombre']}")
    c.drawString(50, 680, "DIRECCION: ")
    c.drawString(400, 680, f" {datos_cliente['direccion']}")
    c.drawString(50, 660, "CORREO ELECTRONICO: ")
    c.drawString(400, 660, f" {datos_cliente['correo']}")
    
    c.drawImage(nombreQR,200,400,100,100)

    # Agregar los detalles del pedido
    y_pos = 600
    c.drawString(50, y_pos, "DETALLES DEL PEDIDO:")
    y_pos -= 20

    if tipo_pedido == "personalizada":
        c.drawString(50, y_pos, "Ingredientes:")
        y_pos -= 15
        for ingrediente in datos_pedido['ingredientes']:
            c.drawString(70, y_pos, f"- {ingrediente}")
            y_pos -= 15

        c.drawString(50, y_pos, f"Tamaño: {datos_pedido['tamano']}")
        y_pos -= 15

        if datos_pedido.get('bebidas'):
            c.drawString(50, y_pos, "Bebidas:")
            y_pos -= 15
            for bebida, cantidad, precio_total in datos_pedido['bebidas']:
                c.drawString(70, y_pos, f"- {bebida} x{cantidad} - Precio: {precio_total}")
                y_pos -= 15

        if datos_pedido.get('complementos'):
            c.drawString(50, y_pos, "Complementos:")
            y_pos -= 15
            for complemento, cantidad, precio_total in datos_pedido['complementos']:
                c.drawString(70, y_pos, f"- {complemento} x{cantidad} - Precio: {precio_total}")
                y_pos -= 15

    elif tipo_pedido == "receta":
        c.drawString(50, y_pos, f"Receta: {datos_pedido['receta']}")
        y_pos -= 15

        c.drawString(50, y_pos, f"Tamaño: {datos_pedido['tamano']}")
        y_pos -= 15

        if datos_pedido.get('bebidas'):
            c.drawString(50, y_pos, "Bebidas:")
            y_pos -= 15
            for bebida, cantidad, precio_total in datos_pedido['bebidas']:
                c.drawString(70, y_pos, f"- {bebida} x{cantidad} - Precio: {precio_total}")
                y_pos -= 15

        if datos_pedido.get('complementos'):
            c.drawString(50, y_pos, "Complementos:")
            y_pos -= 15
            for complemento, cantidad, precio_total in datos_pedido['complementos']:
                c.drawString(70, y_pos, f"- {complemento} x{cantidad} - Precio: {precio_total}")
                y_pos -= 15

    c.save()
    print("reporte generado-----------------")


