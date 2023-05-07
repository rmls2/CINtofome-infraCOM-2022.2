import socket
from teste_mod_aux import Cliente, Servidor
import datetime
# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_cliente.bind(Cliente().ip_porta)



while True:
    # mensagem do cliente
    horas = datetime.datetime.now().strftime('%H:%M')
    mensagem_cliente = input(f'{horas} cliente: ')
    if mensagem_cliente == 'quit':
        break

    # cliente envia mensagem  para o restaurante 
    Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)

    # resposta do restaurante
    respota_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
    print(horas, respota_restaurante.decode())

"""     if respota_restaurante.decode() == 'digite sua mesa':
        # digite a mesa
        mensagem_cliente = input(f'{horas} cliente: ')
        # cliente envia o número da mesa para o restaurante 
        Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)

        # o restaurante responde solicitando o nome do cliente 
        respota_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
        print(horas, respota_restaurante.decode()) """

    # exibe cardapio do CIntofome para o usuário


socket_cliente.close()
