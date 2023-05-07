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