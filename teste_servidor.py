import socket
from teste_mod_aux import Cliente, Servidor
import datetime
# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_servidor.bind(Servidor().ip_porta)

print('CINto fome está aberto esperando receber clientes! :)')


# mensagem do servidor
horas = datetime.datetime.now().strftime('%H:%M')
mensagem_servidor = 'CIntofome: digite sua mesa'

# envia mensagem para o cliente
Servidor().resposta_restaurante(socket_servidor,mensagem_servidor )

socket_servidor.close()

