import random

listaBebidasgrandes = [
    "1. coca cola",
    "2. fanta",
    "3. 7up",
    "4. jarrito (piña)",
    "5. jarrito (tuti frutti)",
    "6. jarrito (mandarina)",
    "7. jarrito (tamarindo)",
    "8. pepsi",
    "9. sidral",
    "10. sprite"]
listaBebidasPequeñas = [
    "11. delaware",
    "12. pepsi",
    "13. DrPepper",
    "14. fresca",
    "15. sidral",
    "16. coca cola",
    "17. jumex",
    "18. boing(mango)",
    "19. boing(guayaba)",
    "20.fanta"]



lista_Precios_BebidasGrandes = [
    
    45,    # Precio de coca cola
    27,    # Precio de fanta
    36,    # Precio de 7up
    32,    # Precio de jarrito (piña)
    32,    # Precio de jarrito (tuti frutti)
    32,    # Precio de jarrito (mandarina)
    32,    # Precio de jarrito (tamarindo)
    38,    # Precio de pepsi
    37,    # Precio de sidral
    37     # Precio de sprite
]

# Lista de precios de bebidas pequeñas
lista_Precios_BebidasPequeñas = [
    
    15,     # Precio de delaware
    15,     # Precio de pepsi
    16.50,  # Precio de DrPepper
    16,     # Precio de fresca
    16,     # Precio de sidral
    17,     # Precio de coca cola (dieta)
    13,     # Precio de jumex
    13.50,  # Precio de boing(mango)
    13.50,   # Precio de boing(guayaba)
    16      # precio fanta 

]

def listaBebidas():
    listaBebidasgrandes,listaBebidasPequeñas

def listaComplementos():
    return[
    "1-palitos de pan",
    "2-nuggets",
    "3-bonelees diablo ",
    "4-bonelees mango",
    "5-bonelees bufalo",
    "6-bonelees BBQ",
    "7-bonelees chicago",
    "8-bonelees california",
    "9-bonelees vegana",
    "10-bonelees habanero",
    "11-bonelees chipotle",
    "12-bonelees BBQ mango",
    "13-ensalada griega",
    "14-ensalada de pasta ",
    "15-ensalada de papa ",
    "16-ensalda mixta ",
    "17-ensalada caprese",
    "18-ensalada waldorf",
    "19-ensalada rusa ",
    "20-ensalada de col",
    ]
    


def listaRecetas():
    return[
    "1-hawaina",
    "2-peperoni",
    "3-carnes frias",
    "3-mexicana",
    "4-champiñones",
    "5-margarita ",
    "6-cuatro quesos",
    "7-cuatro estaciones",
    "8-marinara",
    "9-napolitana",
    "10-neoyorquina",
    "11-fugazza",
    "12-pollo",
    "13-carbonara",
    "14-barbacoa",
    "15-prosciutto ",
    "16-calzone",
    "17-caprichosa",
    "18-pizza de pera ",
    "19-anchoas",
    "20-salmon ",
    "21-caprese",
    "22-pizza blanca ",
    "23-BBQ",
    "24-vegetariana",
    "25-libre de gluten",
    "26-maltesa",
    "27-atun",
    "28-griega",
    "29-saint louis",
    "30-stromboli"]

def generar_codigo_rastreo():
    return str(random.randint(1000000, 9999999))

no_pedido = generar_codigo_rastreo()

def listacombos():
    return[
    "1-Combo familiar",
    "2-Combo mini pizza",
    "3-Combo cuadrada ",
    "4-Combo alitas",
    "5-Combo ensaldas",]



def obtener_lista_ingredientes():
    return [
    "peperoni",
    "champiñones",
    "chorizo",
    "jamon",
    "piña",
    "tocino",
    "salchica",
    "pimiento verde",
    "aceitunas",
    "salami",
    "cebolla",
    "jitomate",
    "extra queso",
    "atun",
    "ajonjoli",
    "moztaza",
    "aguacate",
    "jalapeños",
    "pera",
    "pollo",
    "frijol",
    "arandanos",
    "arrachera",
    "mozarela",
    "gouda",
    "carne molida",
    "maiz",
    "albahaca",
    "anchoas",
    "salmon",
    "bistec",
    "calabaza"]
    
def obtener_lista_Tamanos():
    return[
    "chica",
    "mediana",
    "grande",
    "familiar",
    "mini pizza (docena)",
    "cuadrada"]

lista_Precios_Tamanos = [
    200,
    275,
    305,
    329,
    305,
    375
]