import socket
from modulo_aux import Cliente, Servidor, cardapio, opcoes
import datetime
import time
# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_cliente.bind(Cliente().ip_porta)

cardapio_comidas = cardapio()
# cardapio_bebidas = Servidor().cardapio()[1]

opcoes = opcoes()


while True:
    # mensagem do cliente
    horas = datetime.datetime.now().strftime('%H:%M')
    mensagem_cliente = input(f'{horas} Cliente: ')
    if mensagem_cliente[:5] == 'nome:':
        Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
        resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
        print(horas, resposta_restaurante.decode())
        break
    # cliente envia mensagem  para o restaurante 
    Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
    # resposta do restaurante
    resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    print(horas, resposta_restaurante.decode())


# parte dois ter que escolher opções dos clientes 
mensagem_cliente = input(f'{horas} Cliente: ')

# lidando com a escolha do menu de opções 
if (mensagem_cliente in opcoes.keys()) or ( mensagem_cliente in opcoes.values()):
    Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
    #resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    # print(horas, resposta_restaurante.decode())
    resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    print(horas, resposta_restaurante.decode())

# lidando com a escolha do cardápio
mensagem_cliente = input(f'{horas} Cliente: ')
if mensagem_cliente == 'pedir':
    Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
    resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    print(horas, resposta_restaurante.decode())

# escolhendo um pedido no cardápio
if mensagem_cliente in cardapio_comidas.keys():
    Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
    resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    print(horas, resposta_restaurante.decode())

    # respondendo ao servidor enquanto houver pedidos para serem feitos 
    while True:
        mensagem_cliente = input(f'{horas} Cliente: ')
        if mensagem_cliente == 'não':
            Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
            resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
            print(horas, resposta_restaurante.decode())
            break
        Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
        resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
        print(horas, resposta_restaurante.decode())

# parte 3 pedir a conta da mesa, pedir a conta individual, levantar, pagar  
mensagem_cliente = input(f'{horas} Cliente: ')
Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
print(horas, resposta_restaurante.decode())

# valor da conta
resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
print(horas, resposta_restaurante.decode())

resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
print(horas, resposta_restaurante.decode())

# ação de pagar o restaurante
mensagem_cliente = input(f'{horas} Cliente: ')
Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)
resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
print(horas, resposta_restaurante.decode())

# pagando o restaurante
mensagem_cliente = input(f'{horas} Cliente: ')
socket_cliente.sendto(mensagem_cliente.encode(), Servidor().ip_porta)

while True:
    resposta_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    print(horas, resposta_restaurante.decode())
    if resposta_restaurante.decode() == 'CINtofome: Obrigado!':
        break
    else:
        mensagem_cliente = input(f'{horas} Cliente: ')
        socket_cliente.sendto(mensagem_cliente.encode(), Servidor().ip_porta)

socket_cliente.close()

