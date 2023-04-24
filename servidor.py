import socket
from modulo_auxiliar import Servidor as servidor, Cliente as cliente


HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5030            # Porta que o Servidor vai ouvir para receber os pacotes
orig = (HOST, PORT)  # contém meu ip e minha porta de origem
dest = (HOST, 3000)  # o destino do servidor é o endereço de origem do cliente

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai ouvir (ip, porta) e vai alocar reserva de buffer para que servidor possa receber os dados passados a ela
socket_serv.bind(servidor().IP_PORTA_servidor)

# recebendo mensagem do cliente
if servidor().inicia:
    print('***servidor inicializado***\n')

    servidor().recebe_pacote(socket_serv, './arqvs_servidor/arquivo_servidor')
    print('\n**retransmitindo pacotes**\n')
    servidor().envia_pacote(
        socket_serv, './arqvs_servidor/arquivo_servidor', cliente().IP_PORTA_cliente)

socket_serv.close()
