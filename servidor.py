import socket

from modulo_auxiliar import Cliente, Servidor

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_servidor.bind(Servidor().ip_porta)

print('***servidor inicializado***\n')

extensao_arquivo, addr = socket_servidor.recvfrom(1024)


if extensao_arquivo:
    caminho_completo = './arqvs_servidor/arquivo_servidor' + extensao_arquivo.decode()

    Servidor().recebe_pacote(socket_servidor, caminho_completo)

    print('\n**retransmitindo pacotes**\n')

    Servidor().envia_pacote(socket_servidor, caminho_completo, Cliente().ip_porta)

else:
    Servidor().recebe_pacote(socket_servidor, './arqvs_servidor/arquivo_servidor')

    print('\n**retransmitindo pacotes**\n')

    Servidor().envia_pacote(socket_servidor, './arqvs_servidor/arquivo_servidor', Cliente().ip_porta)

socket_servidor.close()
