import socket
from teste_mod_aux import Cliente, Servidor
import datetime
# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_cliente.bind(Cliente().ip_porta)

# mensagem do cliente
horas = datetime.datetime.now().strftime('%H:%M')
mensagem_cliente = input(f'{horas} cliente: ')

# cliente envia mensagem  para o servidor 
Cliente().solicitacao_cliente(socket_cliente, Servidor().ip_porta, mensagem_cliente)

respota_restaurante, addr_restaurante = socket_cliente.recvfrom(1024)
print(horas, respota_restaurante.decode())

socket_cliente.close()
