import time
import hashlib
import sys

HOST = 'localhost'  # Endereco IP do Servidor
PORT_serv = 5000    # porta que o Servidor vai ouvir para receber os pacotes
port_clnt = 3010


class Servidor():
    def __init__(self) -> None:
        self.IP_PORTA_servidor = (HOST, PORT_serv)
        self.inicia = True

    def recebe_pacote(self, socket, caminho_do_arquivo):
        global addr
        arquivo_servidor = open(caminho_do_arquivo, 'wb')
        # mensagem(recebe os dados do pacote), addr recebe a tupla (ip, porta), onde porta é o numero de porta do transmissor
        # #1024 representa o tamanho do pacote recebido
        mensagem, addr = socket.recvfrom(1024)

        try:
            while mensagem:
                # Separa o número de sequência, o checksum e os dados do pacote
                num_sequencia, checksum, dados = mensagem.decode().split('|')

                print(addr, dados)
                # Verifica o checksum
                if hashlib.md5(dados.encode()).hexdigest() == checksum:
                    # se o checksum bater ele vai escrever os dados no arquivo do servidor
                    arquivo_servidor.write(dados.encode())
                    print(f'pacote {num_sequencia} chegou corretamente...')
                else:
                    print(f'pacote {num_sequencia} corrompido...')
                # gera uma execeção após um tempo de 2 caso o o receptor em questão não receba mais pacotes
                socket.settimeout(2)
                mensagem, addr = socket.recvfrom(1024)
        except TimeoutError:
            print('transmissão finalizada!')

        arquivo_servidor.close()

    def envia_pacote(self, socket, caminho_do_arquivo, ip_porta):
        arquivo = open(caminho_do_arquivo, 'rb')
        num_sequencia = 1
        while True:
            dados = arquivo.read(1024)
            if not dados:
                break
            # Calcula o checksum
            checksum = hashlib.md5(dados).hexdigest()
            # Monta a mensagem com número de sequência, checksum e dados do pacote
            mensagem = f'{num_sequencia}|{checksum}|'.encode() + dados
            # envia para o o socket (ip, porta)
            socket.sendto(mensagem, ip_porta)
            print(f'enviando pacote {num_sequencia}...')
            num_sequencia += 1
            time.sleep(0.0001)
        print('transmissão finalizada!')
        arquivo.close()


class Cliente():
    def __init__(self) -> None:
        self.IP_PORTA_cliente = (HOST, port_clnt)
        self.inicia = True

    def recebe_pacote(self, socket, caminho_do_arquivo):
        global addr
        arquivo_servidor = open(caminho_do_arquivo, 'wb')
        # mensagem(recebe os dados do pacote), addr recebe a tupla (ip, porta), onde porta é o numero de porta do transmissor
        # #1024 representa o tamanho do pacote recebido
        mensagem, addr = socket.recvfrom(1024)

        try:
            while True:

                # Separa o número de sequência, o checksum e os dados do pacote
                num_sequencia, checksum, dados = mensagem.decode().split('|')
                # Verifica o checksum
                if hashlib.md5(dados.encode()).hexdigest() == checksum:
                    # se o checksum bater ele vai escrever os dados no arquivo do servidor
                    arquivo_servidor.write(dados.encode())
                    print(f'pacote {num_sequencia} chegou corretamente...')
                else:
                    print(f'pacote {num_sequencia} corrompido...')
                # gera uma execeção após um tempo de 2 caso o o receptor em questão não receba mais pacotes
                socket.settimeout(2)
                mensagem, addr = socket.recvfrom(1024)
        except TimeoutError:
            print('transmissão finalizada!')

        arquivo_servidor.close()

    def envia_pacote(self, socket, caminho_do_arquivo, ip_porta):
        arquivo = open(caminho_do_arquivo, 'rb')
        num_sequencia = 1
        while True:
            dados = arquivo.read(1024)
            if not dados:
                break
            # Calcula o checksum
            checksum = hashlib.md5(dados).hexdigest()
            # Monta a mensagem com número de sequência, checksum e dados do pacote
            mensagem = f'{num_sequencia}|{checksum}|'.encode() + dados
            socket.sendto(mensagem, ip_porta)
            print(f'enviando pacote {num_sequencia}...')
            num_sequencia += 1
            time.sleep(0.0001)
        print('transmissão finalizada!')
        arquivo.close()
