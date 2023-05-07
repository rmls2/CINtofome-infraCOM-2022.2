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

informacoes_cliente = []

while True:

    dados = Servidor().recebe_solicitacao(socket_servidor)
    
    if dados.decode()[0:6] == 'nome: ':
        informacoes_cliente.append(dados.decode()[6:])
    if dados.decode() in Servidor().mesas:
        informacoes_cliente.append(dados.decode())
    print(informacoes_cliente)
    try:
        socket_servidor.settimeout(5)
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
       
    except TimeoutError:
        print('comunicação finalizada')
        break

informacoes_cliente.append(Cliente().ip_porta)
print(informacoes_cliente)

socket_servidor.close() 

