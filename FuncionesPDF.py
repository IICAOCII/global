from reportlab.pdfgen import canvas


ruta = "C:/Users/Lenovo/Desktop/prueba funciones/prubea funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"

def generarPDF(listaNombres, listaEdades):
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    c.setFont('Helvetica',20)
    c.drawString(xInicial,yInicial,"edad")
    c.drawString(xInicial + 120 ,yInicial,"nombre")
    for i in range(len(listaNombres)):
        c.setFont('Helvetica',18)
        yInicial = yInicial -20 
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombres[i])
    c.save()
    print("reporte generado-----------------")


