import json

# Criando o arquivo JSON vazio
with open('teste.json', 'w') as f:
    json.dump({}, f)
    print('json criado')
    print('-----------------------------------------------------------------------')

# Função para carregar os dados do arquivo JSON
def load_data():
    with open('teste.json', 'r') as f:
        data = json.load(f)
    return data

# Função para salvar os dados no arquivo JSON
def save_data(data):
    with open('teste.json', 'w') as f:
        json.dump(data, f, indent=4)

def dados_do_cliente(nome, mesa, socket, *conta_individual, **pedidos):
    cliente =  {"id": nome, "mesa": mesa, "conta individual": conta_individual,"socket": socket,"pedidos": pedidos}
    return cliente

def opcoes():
    opcoes_restaurante = {1:'cardápio', 2: 'pedido', 3: 'conta individual', 5 :'nada não, tava só testando', 6:'conta da mesa'}
    return opcoes_restaurante

def cardapio():
    comidas = {
    'lasanha': 25.00,
    'strogonoff': 30.00,
    'risoto': 20.00,
    'hamburguer': 18.00,
    'pizza': 35.00,
    'sopa': 15.00,
    'salada': 12.00
    }
    bebidas = {
    'água': 3.00,
    'refrigerante': 5.00,
    'cerveja': 6.00,
    'suco': 8.00,
    'café': 4.00,
    'chá': 4.00,
    'vinho': 30.00
    }

    lista_cardapio = [comidas, bebidas]
    return lista_cardapio

# Criando os objetos descritos
servicos = {
    1: 'cardapio',
    2: 'Pedido',
    3: 'conta individual',
    3: 'conta da mesa'
}

pedido = {
    "id": "Joao",
    "mesa": 5,
    "conta individual": [2,1,3],
    "socket": ("localhost", 3000),
    "pedidos": {
        "produto1": 2,
        "produto2": 1,
        "produto3": 3
    }
}

pedido_2 = {
    "id": "Marcelo",
    "mesa": 5,
    "conta individual": [2,1,3],
    "socket": ("localhost", 3000),
    "pedidos": {
        "produto1": 2,
        "produto2": 1,
        "produto3": 3
    }
}

pedido_3 = {
    "id": "Marcos",
    "mesa": 5,
    "conta individual": [2,1,3],
    "socket": ("localhost", 3000),
    "pedidos": {
        "produto1": 2,
        "produto2": 1,
        "produto3": 3
    }
}


# Carregando os dados do arquivo JSON
data = load_data()
data['pedido'] = pedido
save_data(data)

data = load_data()
data['pedido 2'] = pedido_2
save_data(data)

data= load_data()
data['pedido 3'] = pedido_3
save_data(data)

data=load_data()
data['pedido 4'] = dados_do_cliente('robert', 5,("localhost", 3000),*[2,1,3], **{"produto1": 2,"produto2": 1,"produto3": 3})
save_data(data)

data=load_data()
data['pedido 5'] = dados_do_cliente('karol',5, ('localhost', 3000), *[50.0, 10.0],**{'bife': 50.0, 'suco': 10.00} )
save_data(data)
""" del data['pedido 5']
save_data(data) """

# del data['pedido']['socket']
# save_data(data) 

""" # excluindo o pedido
del data_2["pedido 2"]
#del data["pedido"]

save_data(data_2)
save_data(data) """

# Adicionando os objetos no arquivo JSON
# data['servicos'] = servicos
#data['pedido'] = pedido
#data_2['pedido 2'] = pedido_2


# Salvando os dados no arquivo JSON
#save_data(data)
#save_data(data_2)
# Exibindo o conteúdo do arquivo JSON
#print('esse são os dados do json:', data_2)

# Alterando uma informação
# data['servicos'][1] = 'Barbearia'
#save_data(data)

# Adicionando uma informação
#data['pedido']['pedidos']['produto4'] = 8.5
#save_data(data)

# Excluindo uma informação
# del data['servicos'][3]
# save_data(data)

#del data['servicos'][1]
# Exibindo o conteúdo atualizado do arquivo JSON




  
