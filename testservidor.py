import socket
from modulo_aux import inicia_servidor, recebe_mensagem, envia_mensagem, recebe_arquivo, envia_arquivo
import time

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor vai ouvir para receber os pacotes
orig = (HOST, PORT)  # contém meu ip e minha porta de origem
dest = (HOST, 3000)  # o destino do servidor é o endereço de origem do cliente

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
udp_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do servidor possa receber os dados passados a ela
udp_serv.bind(orig)

# recebendo mensagem do cliente

if inicia_servidor() == 'mensagem':
    # esse loop vai iterar enquanto o cliente enviar os pacotes
    while True:
       # mensagem_client, client_Addr = udp_serv.recvfrom(1024)
        # print(client_Addr, mensagem_client.decode())
        mensagem_client = recebe_mensagem(udp_serv)
        print(dest, mensagem_client)

        if mensagem_client == 'quit servidor':
            print('servidor finalizado')
            break
        envia_mensagem(udp_serv, mensagem_client, dest)
else:
    # recebendo arquivo do cliente
    arqv = input('digite um nome p/ o arquivo a ser recebido: ')
    extensao = input('digite agora a extensão do arquivo: ')

    arqv = arqv + extensao
    recebe_arquivo(udp_serv, arqv)

    # manda para o cliente qual vai ser a extensão do arquivo que o servidor mandará ao cliente
    udp_serv.sendto(extensao.encode(), ('localhost', 3000))
    envia_arquivo(udp_serv, arqv, dest)

# finaliza o socket
udp_serv.close()
