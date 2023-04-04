import socket
import time
from modulo_aux import data_msg, arquivo, inicia_cliente  # importar modulo auxiliar

HOST = 'localhost'  # ip do servidor
PORT = 5000  # porta onde o servidor vai receber os pacotes
dest = (HOST, PORT)

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
udp_client.bind(('localhost', 3000))

# envio de mensagem ao servidor

# a função inicia cliente retorna true para envio de mensagem e false caso o cliente queira enviar um arquivo
if inicia_cliente():
    data_msg = input('digite sua mensagem aqui: ')
    # o loop vai iterar até o comando quit cliente seja digitado
    while data_msg != 'quit cliente':
        print('enviando pacote...')
        # envia a mensage codificada em bytes para o servidor destino
        udp_client.sendto(data_msg.encode(), dest)
        # comando para parar o servidor e nesse caso também vai parar o cliente
        if data_msg == 'quit servidor':
            print('cliente finalizado')
            break
        # recebe o dados do socket, um par (bytes, endereço), 1024 representa o tamanho do pacote recebido
        msg_serv, serv_Addr = udp_client.recvfrom(1024)
        # decodifica os bytes recebidos, nesse caso, o método decode() retorna uma string
        msg_serv = msg_serv.decode()
        print(serv_Addr, msg_serv)
        # entrada do usuário para enviar novas mensagens
        data_msg = input('digite sua mensagem aqui: ')
    # verifica se o servidor foi finalizado
    if data_msg == 'quit servidor':
        data_msg = data_msg
    else:
        print('cliente finalizado')

#  envio de arquivo ao servidor

else:
    arquivo = input('passe o caminho do arquivo aqui:')
    # abre o arquivo que será enviado pelo servidor
    file = open(arquivo, 'rb')
    # o método read(1024) vai fazer a leitura dos primeiros 1024 bytes do arquivo
    data = file.read(1024)

    while data:
        # envia a mensage codificada em bytes para o servidor destino
        udp_client.sendto(data, dest)
        #gera um pequeno atraso antes da leitura do próximo pacote, para não sobreescrever bytes
        time.sleep(0.001)
        # vai fazer a leitura dos próximos 1024 bytes do arquivo, se houver.
        data = file.read(1024)
        print('enviando pacote...')
    # fehca o arquivo aberto na linha 50
    file.close()
    print('arquivo enviado com sucesso!')

    # arquivo recebido do servidor

    
    # recebe primeiro a extensão do arquivo que será enviado
    extensao, serv_Addr = udp_client.recvfrom(1024)
    #decodifica os bytes em string
    extensao = extensao.decode()
    #cria o nome do arquivo com a extensão correta.
    arquivo_retransmitido = 'arquivo-retransmitido'+ extensao
    # abre o arquivo que será retransmitido para a escrita dos bytes enviado pelo servidor
    file_rrecvd = open(arquivo_retransmitido, 'wb')
    # recebe o dados do socket, um par (bytes, endereço), 1024 representa a capacidade do pacote
    data_rrecvd, serv_Addr = udp_client.recvfrom(1024)
    # o bloco try servir para escrever os dados recebido nesse aquivo ate gerar uma exceção de timeout
    # isso vai servir para que quando o servidor termine de transmitir o arquivo guardado o código saia do loop
    try:
        while data_rrecvd:
            print('escrevendo os dados...')
            # escreve os dados no arquivo criado
            file_rrecvd.write(data_rrecvd)
            print('recebendo pacote retransmitido pelo servidor...')
            # define um tempo limite para bloquear operaçoes de socket, gerando a exceção timeout
            udp_client.settimeout(2)
            data_rrecvd, serv_Addr = udp_client.recvfrom(1024)
    except TimeoutError:
        print('arquivo enviado pelo servidor e recebido pelo cliente com sucesso')

    file_rrecvd.close()
# finaliza o socket udp
udp_client.close()
