import socket
from teste_mod_aux import Cliente, Servidor, cardapio, opcoes
import datetime
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

    # respondendo aos pedidos
    
socket_cliente.close()
