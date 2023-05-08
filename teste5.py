
bebidas = {
'água': 3.00,
'refrigerante': 5.00,
'cerveja': 6.00,
'suco': 8.00,
'café': 4.00,
'chá': 4.00,
'vinho': 30.00
}

x = 'água: 3.00'

try:
    x = int(x)
except ValueError:
    pass

print('deu erro')


