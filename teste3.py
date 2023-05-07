# brincando com json

import json

carros_jason = '{"marca": "fiat", "modelo": "palio", "cor": "vermelho"}'

carros = json.loads(carros_jason)  # o objeto agora é da classe dict


""" for k, v in carros.items():
    print(carros_jason) """


""" print(type(carros_jason))
print(type(carros))
 """

# objeto dict
carros = {"marca": "fiat", "modelo": "palio",
          "cor": "vermelho"}  # objeto da classe dict

# o objeto agora é um json, mas a classe é string
carros_jason = json.dumps(carros, indent=8, separators=(':', ' - '), sort_keys=True) # parametros adicionais para modificar a estrutura interna do json

# print(carros_jason)


jogador_1 = '{ "nome": "robert", "altura": "1.87", "habilidades":{"tocar violao": "True", "programar": "True", "gamer": "False"},"estudos":["ensino medio", "graduacao matematica", "graduacao ciencia da computacao"]}'

# jogador_1_json = json.dumps(jogador_1, indent=4, separators=(':', ' = '), sort_keys=True)

jogador_1_dict = json.loads(jogador_1) #transformando o objeto json em um dict

#acessando a chave 'estudos' cujo o valor é uma lista
print(jogador_1_dict["estudos"])
# acessando a chave 'habilidades' cujo o valor é um dicionario
print(jogador_1_dict["habilidades"])
""" 
#imprimindo as chaves do meu dicionario
for c in jogador_1_dict:
    print(c)

print('\n\n')

#imprimindo os itemss (chave-valor) do meu dicitionario
for i in jogador_1_dict.items():
    print(i) """

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

# del data['pedido']['socket']
# save_data(data) 