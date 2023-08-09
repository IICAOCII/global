from reportlab.pdfgen import canvas
from FuncionesQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
ruta = "C:/Users/Lenovo/Desktop/prueba funciones/prubea funciones/"
nombreQR = ruta + "miQR.png"

def generarPDF(listaNombres, listaEdades):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + "reporteGlobal_"+fecha_actual.strftime('%d_%m_%y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "hola desde funcion")
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    c.setFont('Helvetica',20)
    c.drawString(xInicial,yInicial,"edad")
    c.drawString(xInicial + 120 ,yInicial,"nombre")
    
    c.drawImage(nombreQR,200,400,100,100)

    for i in range(len(listaNombres)):
        c.setFont('Helvetica',18)
        yInicial = yInicial -20 
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombres[i])
    c.save()
    print("reporte generado-----------------")


