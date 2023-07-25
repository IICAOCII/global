from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

ruta = "C:/Users/Lenovo/Desktop/prueba funciones/prubea funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"

def generarPDF(listaNombres, listaEdades):
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    for i in range(len(listaNombres)):
        c.drawString(xInicial,yInicial,"hoa desde una funcion ")
        yInicial = yInicial -20 
    c.save()
    print("reporte generado-----------------")


