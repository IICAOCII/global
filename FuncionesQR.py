import qrcode
img = qrcode.make("Hola desde Recursos")
f = open("QRfunciones.png", "wb")
img.save(f)
f.close()