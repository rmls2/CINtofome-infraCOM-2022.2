def cardapio():
    comidas = {
    "lasanha": 25.00,
    "strogonoff": 30.00,
    "risoto": 20.00,
    "hamburguer": 18.00,
    "pizza": 35.00,
    "sopa": 15.00,
    "salada": 12.00 }

    """    bebidas = {
    'água': 3.00,
    'refrigerante': 5.00,
    'cerveja': 6.00,
    'suco': 8.00,
    'café': 4.00,
    'chá': 4.00,
    'vinho': 30.00
    } """
    
    return comidas

x = "strogonoff" 
l = []

for c in cardapio().items():
    print(c)
    print(c[0])


