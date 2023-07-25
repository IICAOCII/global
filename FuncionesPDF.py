from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

ruta = "C:/Users/Lenovo/Desktop/prueba funciones/prubea funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"

def generarPDF():
    c = canvas.Canvas(nombreArchivo)
    c.drawString(200,600,"hola desde una funcion")
    c.save()


