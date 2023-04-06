# modulo criado para gerar uma interface amigavel no terminal para decidir se o cliente vai enviar mensage pura ou arquivo

import time
data_msg = ''
arquivo = None


def inicia_cliente():
    while True:
        entrada = input('deseja mandar uma data_msg para o servidor? (y/n): ')

        if entrada == 'y' or entrada == 'Y':
            global data_msg
            data_msg = 'ok'  # input('digite sua data_msg aqui: ')
            return True
        elif entrada == 'n' or entrada == 'N':
            entrada = input(
                'então você deseja enviar um arquivo para o servidor? (y/n): ')
            if entrada == 'y' or entrada == 'Y':
                global arquivo
                arquivo = 'ok'
                return False
            else:
                print('resposta incorreta, vamos tentar novamente!\n')
                continue

# define que tipo de arquivo será recebido pelo servidor, se vai ser mensagem ou aquivo


def inicia_servidor():

    while True:
        print('Que tipo de pacote o cliente deseja mandar, mensagem ou arquivo?')
        opcao_de_pacote = input('Digite mensagem ou arquivo: ')

        if opcao_de_pacote == 'mensagem':
            return opcao_de_pacote

        elif opcao_de_pacote == 'arquivo':
            return opcao_de_pacote
        else:
            print('opção invalida, vamos tentar novamente!')


# função para envio de arquivo
def envia_arquivo(socket_udp, arquivo, ip_porta):

    file = open(arquivo, 'rb')
    # o método read(1024) vai fazer a leitura dos primeiros 1024 bytes do arquivo
    data = file.read(1024)
    while data:
        # envia a mensage codificada em bytes para o servidor destino
        socket_udp.sendto(data, ip_porta)
        # gera um pequeno atraso antes da leitura do próximo pacote, para não sobreescrever bytes
        time.sleep(0.001)
        # vai fazer a leitura dos próximos 1024 bytes do arquivo, se houver.
        data = file.read(1024)
        print('enviando pacote...')
    # fehca o arquivo aberto na linha
    file.close()
    print('arquivo enviado com sucesso!')

# função para recebimento de arquivo


def recebe_arquivo(socket_udp, arquivo):
    global serv_Addr
    # abre o arquivo que será retransmitido para a escrita dos bytes enviado pelo servidor
    file_reccvd = open(arquivo, 'wb')
    # recebe o dados do socket, um par (bytes, endereço), 1024 representa a capacidade do pacote
    data_rrecvd, serv_Addr = socket_udp.recvfrom(1024)
    # o bloco try servir para escrever os dados recebido nesse aquivo ate gerar uma exceção de timeout
    # isso vai servir para que quando o servidor termine de transmitir o arquivo guardado o código saia do loop
    try:
        while data_rrecvd:
            print('escrevendo os dados...')
            # escreve os dados no arquivo criado
            file_reccvd.write(data_rrecvd)
            print('recebendo pacote retransmitido pelo servidor...')
            # define um tempo limite para bloquear operaçoes de socket, gerando a exceção timeout
            socket_udp.settimeout(2)
            data_rrecvd, serv_Addr = socket_udp.recvfrom(1024)
    except TimeoutError:
        print('arquivo recebido com sucesso')
    # fecha o arquivo
    file_reccvd.close()

# função que vai enviar mensagem pro servidor


def envia_mensagem(socket_udp, mensagem, ip_porta):
    # envia a mensage codificada em bytes para o servidor destino
    socket_udp.sendto(mensagem.encode(), ip_porta)
    print('enviando pacote...')


def recebe_mensagem(socket_udp):
    global serv_Addr
    # recebe o dados do socket, um par (bytes, endereço), 1024 representa o tamanho do pacote recebido
    mensagem_serv, serv_Addr = socket_udp.recvfrom(1024)
    # decodifica os bytes recebidos, nesse caso, o método decode() retorna uma string
    mensagem_serv = mensagem_serv.decode()
    return mensagem_serv
