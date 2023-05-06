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



# Carregando os dados do arquivo JSON
data = load_data()

# Adicionando os objetos no arquivo JSON
data['servicos'] = servicos
data['pedido'] = pedido

# Salvando os dados no arquivo JSON
save_data(data)

# Exibindo o conteúdo do arquivo JSON
print('esse são os dados do json:', data)

# Alterando uma informação
data['servicos'][1] = 'Barbearia'
save_data(data)

# Adicionando uma informação
data['pedido']['pedidos']['produto4'] = 8.5
save_data(data)

# Excluindo uma informação
del data['servicos'][3]
save_data(data)

#del data['servicos'][1]
# Exibindo o conteúdo atualizado do arquivo JSON
print(data)
