import socket
from modulo_aux import data_msg, arquivo, inicia_cliente, envia_arquivo, recebe_arquivo, envia_mensagem, recebe_mensagem

HOST = 'localhost'  # ip do servidor
PORT = 5000  # porta onde o servidor vai receber os pacotes
dest = (HOST, PORT)

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
udp_client.bind(('localhost', 3000))

# a função inicia cliente retorna true para envio de mensagem e false caso o cliente queira enviar um arquivo
if inicia_cliente():
    data_msg = input('digite sua mensagem aqui: ')
    # o loop vai iterar até o comando quit cliente seja digitado
    while data_msg != 'quit cliente':
        envia_mensagem(udp_client, data_msg, dest)
        # verifica se a mensagem é quit servidor, para poder sair do loop
        if data_msg == 'quit servidor':
            print('comunicação finalizada')
            break
        print('retransmissão do servidor:', dest, recebe_mensagem(udp_client))
        # entrada do usuário para enviar novas mensagens
        data_msg = input('digite sua mensagem aqui: ')
else:
    arquivo = input('passe o caminho do arquivo aqui:')
    #  envia o arquivo ao servidor
    envia_arquivo(udp_client, arquivo, dest)
    # recebe a um pacote contendo a extensão do arquivo que será transmitido do servidor para o cliente
    extensao, serv_Addr = udp_client.recvfrom(1024)
    # decodifica os bytes em string
    extensao = extensao.decode()
    # cria o nome do arquivo com a extensão correta.
    arquivo_retransmitido = 'arquivo-retransmitido' + extensao
    recebe_arquivo(udp_client, arquivo_retransmitido)
# finaliza o socket udp
udp_client.close()
