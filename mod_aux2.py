import time


# função para envio de arquivo
def envia_arquivo(socket_udp, dest, arquivo):

    file = open(arquivo, 'rb')
    # o método read(1024) vai fazer a leitura dos primeiros 1024 bytes do arquivo
    data = file.read(1024)
    while data:
        # envia a mensage codificada em bytes para o servidor destino
        socket_udp.sendto(data, dest)
        #gera um pequeno atraso antes da leitura do próximo pacote, para não sobreescrever bytes
        time.sleep(0.001)
        # vai fazer a leitura dos próximos 1024 bytes do arquivo, se houver.
        data = file.read(1024)
        print('enviando pacote...')
    # fehca o arquivo aberto na linha
    file.close()
    print('arquivo enviado com sucesso!')

def recebe_arquivo(socket_udp, arquivo):
    global serv_Addr
    # abre o arquivo que será retransmitido para a escrita dos bytes enviado pelo servidor
    file = open(arquivo, 'wb')
    # recebe o dados do socket, um par (bytes, endereço), 1024 representa a capacidade do pacote
    data_rrecvd, serv_Addr = socket_udp.recvfrom(1024)
    # o bloco try servir para escrever os dados recebido nesse aquivo ate gerar uma exceção de timeout
    # isso vai servir para que quando o servidor termine de transmitir o arquivo guardado o código saia do loop
    try:
        while data_rrecvd:
            print('escrevendo os dados...')
            # escreve os dados no arquivo criado
            file.write(data_rrecvd)
            print('recebendo pacote retransmitido pelo servidor...')
            # define um tempo limite para bloquear operaçoes de socket, gerando a exceção timeout
            socket_udp.settimeout(2)
            data_rrecvd, serv_Addr = socket_udp.recvfrom(1024)
    except TimeoutError:
        print('arquivo enviado pelo servidor e recebido pelo cliente com sucesso')

    file.close()