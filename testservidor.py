import socket
from modulo_aux import data_msg, arquivo
import time

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor vai ouvir para receber os pacotes
orig = (HOST, PORT)  # contém meu ip e minha porta de origem

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
udp_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do servidor possa receber os dados passados a ela
udp_serv.bind(orig)

# define que tipo de arquivo será recebido pelo servidor, se vai ser mensagem ou aquivo
formato_arquivo = input(
    'Digite "mensagem" p/ receber mensagem, ou digite o nome de um arquivo (sem sua extensao): ')

# recebendo mensagem do cliente

if formato_arquivo == 'mensagem':
    # esse loop vai iterar enquanto o cliente enviar os pacotes
    while True:
        # recebe o dados do socket, um par (bytes, endereço), 1024 representa o tamanho do pacote recebido pelo servidor
        msg, client_Addr = udp_serv.recvfrom(1024)
        # decodifica os bytes em string
        msg = msg.decode()
        print(client_Addr, msg)
        # comando para desligar o servidor dado pelo cliente (eu sei, é irreal mas é só uma forma de parar o servidor)
        if msg == 'quit servidor':
            print('servidor finalizado')
            break
        # codifica a mensagem em bytes para enviar para o cliente novamente
        msg = msg.encode()
        # envia o pacote com a mensagem para o cliente
        udp_serv.sendto(msg, ('localhost', 3000))
        print('reenviando o pacote ao cliente...')

else:
    # recebendo arquivo do cliente

    arqv = formato_arquivo
    extensao = input('digite agora a extensão do arquivo')

    arqv = arqv + extensao
    # abre o arquivo para escrita de bytes
    file = open(arqv, 'wb')
    ## data recebe os dados enviados pelo cliente, client_Addr recebe o ip do cliente
    ## data, client_Addr = udp_serv.recvfrom(1024)
    # o bloco try/except será usado para sair do loop quando o cliente para de enviar pacotes
    try:
        # data recebe os dados enviados pelo cliente, client_Addr recebe o ip do cliente
        data, client_Addr = udp_serv.recvfrom(1024)
        while data:
            print('escrevendo os dados')
            # escreve os dados no arquivo criado
            file.write(data)
            # define um tempo limite para bloquear operaçoes de socket, gerando a exceção timeout
            udp_serv.settimeout(2)
            print('recebendo pacote...')
            data, client_Addr = udp_serv.recvfrom(1024)
    except TimeoutError:
        print('Download do arquivo enviado pelo cliente')
    # fecha o arquivo aberto
    file.close()

    # envio do arquivo ao cliente

    # abre o arquivo criado anteriormente para leitura em bytes
    file_resend = open(arqv, 'rb')
    # manda para o cliente qual vai ser a extensão do arquivo que o servidor mandará ao cliente
    udp_serv.sendto(extensao.encode(),('localhost', 3000))
    # faz a leitura do primeiros 1024 bytes do arquivo
    data_resend = file_resend.read(1024)

    # esse loop vai iterar enquanto houver pacotes para reenviar para o cliente
    while data_resend:
        # re-envia o pacote com a mensagem para o cliente
        udp_serv.sendto(data_resend, ('localhost', 3000))
        #gera um pequeno atraso antes da leitura do próximo pacote, para não sobreescrever bytes
        time.sleep(0.001)
        # vai fazer a leitura dos próximos 1024 bytes do pacote se houver
        data_resend = file_resend.read(1024)
        print('enviando pacote ao cliente...')
    # fecha o arquivo aberto acima
    file_resend.close()
    print('arquivo enviado de volta ao cliente com sucesso!')

# finaliza o socket
udp_serv.close()
