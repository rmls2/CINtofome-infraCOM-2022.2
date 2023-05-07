import socket
from teste_mod_aux import Cliente, Servidor
import datetime
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


while True:
    mensagem_cliente, addr_cliente = socket_servidor.recvfrom(1024)
    try:
        socket_servidor.settimeout(5)
        Servidor().resposta_restaurante(socket_servidor,mensagem_cliente, addr_cliente )
        mensagem_cliente, addr_cliente = socket_servidor.recvfrom(1024)
        # envia mensagem para o cliente
        Servidor().resposta_restaurante(socket_servidor,mensagem_cliente, addr_cliente )
    except TimeoutError:
        print('comunicação finalizada')
        break

# envia mensagem para o cliente
""" Servidor().resposta_restaurante(socket_servidor,mensagem_servidor, addr_cliente )

socket_servidor.close() """

