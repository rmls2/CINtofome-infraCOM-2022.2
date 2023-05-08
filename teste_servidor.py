import socket
from teste_mod_aux import Cliente, Servidor, load_data, save_data, cardapio, opcoes, dados_do_cliente, load_tabela, save_tabela
import datetime
import json
import time
# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_servidor.bind(Servidor().ip_porta)

print('***************************************************************')
print('**** CINto fome está aberto esperando receber clientes! :) ****')
print('***************************************************************')
print('***************************************************************')
# mensagem do servidor
horas = datetime.datetime.now().strftime('%H:%M')
mensagem_servidor = 'CIntofome: digite sua mesa'

cardapio_comida = cardapio()
informacoes_cliente = []
preço_por_prato = []
pratos_escolhidos = {}

opcoes = opcoes()

while True:

    dados = Servidor().recebe_solicitacao(socket_servidor)
    
    if dados.decode()[0:6] == 'nome: ':
        informacoes_cliente.append(dados.decode()[6:])
    if dados.decode() in Servidor().mesas:
        informacoes_cliente.append(dados.decode())
    print(informacoes_cliente)

    try:
        socket_servidor.settimeout(10)
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        if dados.decode()[:5] == 'nome:':
            break
       
    except TimeoutError:
        print('comunicação finalizada')
        break

informacoes_cliente.append(Cliente().ip_porta)
print('são esses os dados do cliente:' , informacoes_cliente)


# parte dois ter que apresentar o menu de opções para o cliente

dados = Servidor().recebe_solicitacao(socket_servidor)
dados = dados.decode()

if dados == '1' or dados == 'cardápio':
    with open('cardapio.json', 'w') as f:
        json.dump({}, f)
        print('json criado')

    data = load_data()
    data['cardapio'] = cardapio_comida
    save_data(data)
    data_json = json.dumps(data, indent=4)
    # envia cardápio
    socket_servidor.sendto(data_json.encode(), Cliente().ip_porta)

time.sleep(2)

# recebe o pedido do cliente escolhendo alguma opção do cardápio
dados = Servidor().recebe_solicitacao(socket_servidor)

# o loop vai rodar enquanto o cliente estiver escolhendo pratos 
while True:
    # armazena o pedido do cliente na lista informacoes_cliente
    if dados.decode() in cardapio_comida.keys():
        # add o preço do prato escolhido na lista preço_por_prato
        preço_por_prato.append(cardapio_comida[dados.decode()])
        # add itens ao dicionários pratos_escolhidos de acordo com o prato escolhido 
        pratos_escolhidos[dados.decode()] = cardapio_comida[dados.decode()]
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        print(informacoes_cliente)
    if dados.decode() == 'não':
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        break
    dados = Servidor().recebe_solicitacao(socket_servidor)

#add os preço e os pratos escolhidos pelo cliente na lista que contém as informações dos clientes.
informacoes_cliente.append(preço_por_prato)
informacoes_cliente.append(pratos_escolhidos)

print(informacoes_cliente)


# parte 3 ter que responder os pedidos do cliente por conta da mesa, conta invidual, lavantar, pagar 

# crianco o arquivo jason da tabela de mesa
with open('tabela_de_mesa.json', 'w') as f:
    json.dump({}, f)
    print('tabela em formato json criado')

# carregando a tabela de mesa
tabela = load_tabela()

mesa = informacoes_cliente[0]
nome = informacoes_cliente[1]
socket_= informacoes_cliente[2]
conta_invidual = informacoes_cliente[3]
pedidos = informacoes_cliente[4]

#passando as informações da tabela de mesa de acordo com as informações do cliente.
tabela['conta de '+ informacoes_cliente[1]] = dados_do_cliente(mesa, nome, socket_, *conta_invidual, **pedidos)
save_tabela(tabela)

socket_servidor.close() 

