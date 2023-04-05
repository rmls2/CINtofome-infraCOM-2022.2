import socket
from modulo_aux import inicia_servidor, recebe_mensagem, envia_mensagem, recebe_arquivo, envia_arquivo
import time

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor vai ouvir para receber os pacotes
orig = (HOST, PORT)  # contém meu ip e minha porta de origem
dest = (HOST, 3000)  # o destino do servidor é o endereço de origem do cliente

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
udp_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai ouvir orig e vai alocar reserva de buffer para que servidor possa receber os dados passados a ela
udp_serv.bind(orig)

# recebendo mensagem do cliente

if inicia_servidor() == 'mensagem':
    # esse loop vai iterar enquanto o cliente enviar os pacotes
    while True:
       # armazena os bytes enviados ao servidor
        mensagem_client = recebe_mensagem(udp_serv)
        print(dest, mensagem_client)
        # condicional que vai definir uma condição de parada do servidor (só pra ter um recurso para derrubar o servidor)
        if mensagem_client == 'quit servidor':
            print('servidor finalizado')
            break
        # retransmite a mensagem de volta ao cliente
        envia_mensagem(udp_serv, mensagem_client, dest)
else:
    # define uma variável que vai endereçar os dados que serão enviados pelo servidor
    arqv = input('digite um nome p/ o arquivo a ser recebido: ')
    extensao = input('digite agora a extensão do arquivo: ')
    arqv = arqv + extensao
    # vai receber os bytes enviados pelo servidor e armazená-los no endereço definido na linha 31
    recebe_arquivo(udp_serv, arqv)

    # manda para o cliente qual vai ser a extensão do arquivo snviado
    udp_serv.sendto(extensao.encode(), ('localhost', 3000))
    # retransmite o arquivo enviado pelo cliente.
    envia_arquivo(udp_serv, arqv, dest)
    print('arquivo retransmitido ao cliente com sucesso!')

# finaliza o socket
udp_serv.close()
