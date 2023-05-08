import socket
from modulo_aux import Cliente, Servidor, load_data, save_data, cardapio, opcoes, dados_do_cliente, load_tabela, save_tabela
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
# mensagem padrão do servidor
horas = datetime.datetime.now().strftime('%H:%M')
mensagem_servidor = 'CIntofome: digite sua mesa'

# as variáveis abaixo vai guardar as informações do cliente que será usada para criar a tabela de mesa
cardapio_comida = cardapio()
informacoes_cliente = []
preço_por_prato = []
pratos_escolhidos = {}
total_do_cliente = ''

opcoes_ = opcoes()

# esse loop vai rodar até pegar as informações de nome e mesa do cliente
while True:
    dados = Servidor().recebe_solicitacao(socket_servidor)
    
    if dados.decode()[0:6] == 'nome: ':
        informacoes_cliente.append(dados.decode()[6:])
    if dados.decode() in Servidor().mesas:
        informacoes_cliente.append(dados.decode())
    # print(informacoes_cliente)

    try:
        socket_servidor.settimeout(10)
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        if dados.decode()[:5] == 'nome:':
            break
       
    except TimeoutError:
        print('comunicação finalizada')
        break

#até aqui essa quarda o numero de mesa e o nome do cliente
informacoes_cliente.append(Cliente().ip_porta)

# parte dois: O código abaixo visa apresentar o menu de opções para o cliente 
dados = Servidor().recebe_solicitacao(socket_servidor)
dados = dados.decode()

# o código abaixo cria um arquivo json contendo o cardápio do restaurante
if dados == '1' or dados == 'cardápio':
    with open('cardapio.json', 'w') as f:
        json.dump({}, f)
        # print('json criado')

    # load_data() carrega um arquivo json
    data = load_data()
    # vai referenciar cardapio_comida que guarda um dicionário contendo o conteudo do cardapio
    data['cardapio'] = cardapio_comida
    #salva o cardapio no arquivo json
    save_data(data)
    # converte o dicionario em um arquivo json
    data_json = json.dumps(data, indent=4)
    # envia cardápio que será exibido na tela para o cliente
    socket_servidor.sendto(data_json.encode(), Cliente().ip_porta)

time.sleep(2)

#recebe o pedido do cliente escolhendo alguma opção do cardápio
dados = Servidor().recebe_solicitacao(socket_servidor)

# o loop vai rodar enquanto o cliente estiver escolhendo pratos 
while True:
    # armazena o pedido do cliente na lista informacoes_cliente
    if dados.decode() in cardapio_comida.keys():
        # add o preço do prato escolhido numa lista que guarda o preço dos pratos
        preço_por_prato.append(cardapio_comida[dados.decode()])
        # add itens ao dicionários pratos_escolhidos de acordo com o prato escolhido 
        pratos_escolhidos[dados.decode()] = cardapio_comida[dados.decode()]
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        # print(informacoes_cliente)
    if dados.decode() == 'não':
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        break
    dados = Servidor().recebe_solicitacao(socket_servidor)

#add os preço e os pratos escolhidos pelo cliente na lista que contém as informações dos clientes.
informacoes_cliente.append(preço_por_prato)
informacoes_cliente.append(pratos_escolhidos)

# parte 3: responde aos pedidos do cliente  

# crianco o arquivo jason da tabela de mesa
with open('tabela_de_mesa.json', 'w') as f:
    json.dump({}, f)

# carregando a tabela de mesa
tabela = load_tabela()

# salva as informações do cliente em variáveis que serão usadas para criar o registro do cliente na tabela de mesa 
mesa = informacoes_cliente[0]
nome = informacoes_cliente[1]
socket_= informacoes_cliente[2]
conta_invidual = informacoes_cliente[3]
pedidos = informacoes_cliente[4]

#passa as informações da tabela de mesa de acordo com as informações do cliente para o arquivo json
tabela['conta de '+ informacoes_cliente[1]] = dados_do_cliente(mesa, nome, socket_, *conta_invidual, **pedidos)
save_tabela(tabela)

# parte 4: fase de pagamento do cliente, tendo o cliente ja escolhido o(s) seu(s) pedido(s) 
dados = Servidor().recebe_solicitacao(socket_servidor)
Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)

# calcular a conta do cliente de acordo com o que foir armazenado na tabela de mesa 
if dados.decode() == 'quanto custou?':
    conta_a_pagar = tabela['conta de '+ informacoes_cliente[1]]["conta individual"]
    pedidos = tabela['conta de '+ informacoes_cliente[1]]["pedidos"]
    total_a_pagar = 0
    for c in conta_a_pagar:
        total_a_pagar+=c
    total_do_cliente = str(total_a_pagar)

    # envia para o cliente o histórico dos seus pedidos 
    pedidos_json = json.dumps(pedidos, indent=4)
    socket_servidor.sendto(pedidos_json.encode(), Cliente().ip_porta)
    # informa ao cliente o total a pagar
    socket_servidor.sendto(f'CIntofome: o total é {total_do_cliente}'.encode(), Cliente().ip_porta)

# parte 5: pagamento do cliente, recebe a intenção de pagamento
dados = Servidor().recebe_solicitacao(socket_servidor)
Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)

# recebendo o pagamento do cliente, caso ele erre o pagamento, o loop o obriga a fornecer o pagamento correto  
while True:
    if dados.decode() == 'pagar':
        pagamento_cliente, addr_cliente = socket_servidor.recvfrom(1024)

        if pagamento_cliente.decode() == total_do_cliente:
            socket_servidor.sendto('CINtofome: Obrigado!'.encode(), Cliente().ip_porta)
            break
        else:
            socket_servidor.sendto('CINtofome: Digitou o valor errado. Tente novamente'.encode(), Cliente().ip_porta)
            pagamento_cliente, addr_cliente = socket_servidor.recvfrom(1024)

#apagando o registro do cliente na tabela de mesa
del tabela['conta de '+ informacoes_cliente[1]]
save_tabela(tabela)

socket_servidor.close() 

