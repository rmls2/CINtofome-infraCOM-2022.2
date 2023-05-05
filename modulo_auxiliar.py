import time
from datetime import datetime


class Cliente ():
    def __init__(self) -> None:
        self.ip_porta = ('localhost', 3001)

    def envia_pacote(self, socket, caminho_do_arquivo, ip_porta):
        arquivo = open(caminho_do_arquivo, 'rb')
        num_sequencia = 1

        while True:
            dados = arquivo.read(1024)
            dados_em_bits = ''.join([format(byte, '08b') for byte in dados])
            if not dados:
                break
            # Monta a mensagem com número de sequênciextensao_arquivo = input('digite a extensão do arquivo enviado: ')a, checksum e dados do pacote
            mensagem = f'{bin(num_sequencia)}|-x-|-x-|-x-|{self.checksum(dados_em_bits)}|-x-|-x-|-x-|'.encode(
            )+dados

            # start_timer = datetime.now()
            # envia para o o socket (ip, porta)
            socket.sendto(mensagem, ip_porta)

            print(f'\nenviando pacote {num_sequencia}...')

            print(self.recebe_ack(socket))

            # end_timer = datetime.now()
            # time_taken = (end_timer - start_timer).total_seconds()
            # print('tempo de envio de pacote e recebimento de ack: {:.8f} segundos'.format(time_taken))

            num_sequencia += 1
            time.sleep(0.0001)
        print('transmissão finalizada!')
        arquivo.close()

    def recebe_pacote(self, socket, caminho_do_arquivo):
        global addr
        arquivo_servidor = open(caminho_do_arquivo, 'wb')
        # mensagem(recebe os dados do pacote), addr recebe a tupla (ip, porta), onde porta é o numero de porta do transmissor
        # #1024 representa o tamanho do pacote recebido
        mensagem, addr = socket.recvfrom(2048)
        socket.settimeout(0.05)

        try:
            while mensagem:
                # Separa o número de sequência, o checksum e os dados do pacote
                num_sequencia, checksumm, dados = mensagem.split(
                    '|-x-|-x-|-x-|'.encode())
                num_sequencia = num_sequencia.decode()
                checksumm = checksumm.decode()

                dados_em_bits = ''.join([format(byte, '08b')
                                        for byte in dados])

                if checksumm == self.checksum(dados_em_bits):
                    print(
                        f'pacote {int(num_sequencia[2:], 2)} recebido.')
                    arquivo_servidor.write(dados)
                else:
                    print(f'pacote {int(num_sequencia[2:], 2)} corrompido...')
                # gera uma execeção após um tempo de 2 segundos caso o receptor em questão não receba mais pacotes
                # socket.settimeout(1)
                mensagem, addr = socket.recvfrom(2048)

        except TimeoutError:
            print('transmissão finalizada!')

        arquivo_servidor.close()

    def checksum(self, dados):
        groups = [dados[i:i+8] for i in range(0, len(dados), 8)]
        binaries = [int(group, 2) for group in groups]
        soma_dados = sum(binaries)

        return bin(soma_dados)[2:]

    def envia_ack(self, socket, mensagem, num_seq, addr):
        if mensagem:
            ack = f'ACK {int(num_seq[2:], 2)}'
            socket.sendto(ack.encode(), addr)
            return f'- enviando {ack}\n'

    def recebe_ack(self, socket):
        global addr
        mensagem, addr = socket.recvfrom(512)
        mensagem = mensagem.decode()

        if mensagem:
            return f'- {mensagem} recebido\n'


class Servidor():
    def __init__(self) -> None:
        self.ip_porta = ('localhost', 5000)

    def envia_pacote(self, socket, caminho_do_arquivo, ip_porta):
        arquivo = open(caminho_do_arquivo, 'rb')
        num_sequencia = 1

        while True:
            dados = arquivo.read(1024)
            dados_em_bits = ''.join([format(byte, '08b') for byte in dados])

            if not dados:
                break
            # Monta a mensagem com número de sequência, checksum e dados do pacote
            mensagem = f'{bin(num_sequencia)}|-x-|-x-|-x-|{self.checksum(dados_em_bits)}|-x-|-x-|-x-|'.encode(
            )+dados
            # envia para o o socket (ip, porta)
            socket.sendto(mensagem, ip_porta)
            print(f'enviando pacote {num_sequencia}...')
            num_sequencia += 1
            time.sleep(0.0001)
        print('transmissão finalizada!')
        arquivo.close()

    def recebe_pacote(self, socket, caminho_do_arquivo):
        global addr
        arquivo_servidor = open(caminho_do_arquivo, 'wb')
        # mensagem(recebe os dados do pacote), addr recebe a tupla (ip, porta), onde porta é o numero de porta do transmissor
        # #1024 representa o tamanho do pacote recebido
        mensagem, addr = socket.recvfrom(2048)
        socket.settimeout(0.05)
        try:
            while mensagem:
                # Separa o número de sequência, o checksum e os dados do pacote
                num_sequencia, checksumm, dados = mensagem.split(
                    '|-x-|-x-|-x-|'.encode())
                num_sequencia = num_sequencia.decode()
                checksumm = checksumm.decode()

                # self.envia_ack(socket, mensagem,num_sequencia,addr)

                dados_em_bits = ''.join([format(byte, '08b')for byte in dados])

                if checksumm == self.checksum(dados_em_bits):
                    print(f'pacote {int(num_sequencia[2:], 2)} recebido.')
                    print(self.envia_ack(socket, mensagem, num_sequencia, addr))
                    arquivo_servidor.write(dados)
                else:
                    print(f'pacote {int(num_sequencia[2:], 2)} corrompido...')
                # gera uma execeção após um tempo de 2 caso o o receptor em questão não receba mais pacotes
                # socket.settimeout(1)
                mensagem, addr = socket.recvfrom(2048)
        except TimeoutError:
            print('transmissão finalizada!')

        arquivo_servidor.close()

    def checksum(self, dados):
        groups = [dados[i:i+8] for i in range(0, len(dados), 8)]
        binaries = [int(group, 2) for group in groups]
        soma_dados = sum(binaries)

        return bin(soma_dados)[2:]

    def envia_ack(self, socket, mensagem, num_seq, addr):
        if mensagem:
            ack = f'ACK {int(num_seq[2:], 2)}'
            socket.sendto(ack.encode(), addr)
            return f'- enviando {ack}\n'

    def recebe_ack(self, socket):
        global addr
        mensagem, addr = socket.recvfrom(512)
        mensagem = mensagem.decode()

        if mensagem:
            return f'- {mensagem} recebido\n'
