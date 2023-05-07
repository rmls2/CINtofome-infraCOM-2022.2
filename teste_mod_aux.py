import time

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
            # Monta a mensagem com número de sequência, dados e checksum
            mensagem = f'{bin(num_sequencia)}|-x-|-x-|-x-|{self.checksum(dados_em_bits)}|-x-|-x-|-x-|'.encode()+dados
           # Defina o número máximo de reenvios
            MAX_RESENDS = 3
            # Defina o tempo limite para a resposta do servidor (em segundos)
            TIMEOUT = 1
            # Enquanto o número de reenvios for menor que o máximo permitido
            for i in range(MAX_RESENDS):
                # Envie o pacote e imprima a mensagem
                socket.sendto(mensagem, ip_porta)
                print(f"\nEnviando pacote {num_sequencia}...")
                # Inicie o temporizador
                start_time = time.time()
                # Enquanto o tempo limite não for atingido
                while (time.time() - start_time) < TIMEOUT:
                    # Aguarde a resposta do servidor
                    try:
                        socket.settimeout(TIMEOUT)
                        if self.recebe_ack(socket):
                            print(f'- ACK {num_sequencia} recebido')
                            break
                    except TimeoutError:
                        print(f"Tempo limite atingido para o pacote {num_sequencia}!")
                # Se o ACK foi recebido, encerre o loop de reenvio e o programa
                if self.recebe_ack != None:
                    break
                # Se o tempo limite for atingido e o ACK não for recebido, reenvie o pacote
                print(f"ACK não recebido para o pacote {num_sequencia}. Tentando novamente...")

            num_sequencia += 1
            time.sleep(0.0001)

        print('transmissão finalizada!')
        arquivo.close()

    def solicitacao_cliente(self,socket,addr_restaurante, mensagem):
        global num_sequencia
        num_sequencia = 1
        dados_em_bits = ''.join([format(byte, '08b') for byte in mensagem.encode()])

        # Monta a mensagem com número de sequência, dados e checksum
        pacote = f'{bin(num_sequencia)}|-x--x-|{self.checksum(dados_em_bits)}|-x--x-|{mensagem}'.encode()
        MAX_RESENDS = 3
        # Defina o tempo limite para a resposta do servidor (em segundos)
        TIMEOUT = 1

        # Enquanto o número de reenvios for menor que o máximo permitido
        for i in range(MAX_RESENDS):
            # Envie o pacote e imprima a mensagem
            socket.sendto(pacote, addr_restaurante)
            # print(f"\nEnviando pacote {num_sequencia}...")
            # Inicie o temporizador
            start_time = time.time()
             # Enquanto o tempo limite não for atingido
            while (time.time() - start_time) < TIMEOUT:
                # Aguarde a resposta do servidor
                try:
                    socket.settimeout(TIMEOUT)
                    if self.recebe_ack(socket):
                        # print(f'- ACK {num_sequencia} recebido')
                        break
                except TimeoutError:
                    print(f"Tempo limite atingido para o pacote {num_sequencia}!")
            if self.recebe_ack(socket)!= None:
                break
        num_sequencia+=1


    def recebe_pacote(self, socket, caminho_do_arquivo):
        arquivo_servidor = open(caminho_do_arquivo, 'wb')
        # mensagem(recebe os dados do pacote), addr recebe a tupla (ip, porta), 1024 representa o tamanho do pacote recebido
        mensagem, addr = socket.recvfrom(2048)
        socket.settimeout(0.05)

        try:
            while True:
                # Separa o número de sequência, o checksum e os dados do pacote
                num_sequencia, checksumm, dados = mensagem.split('|-x-|-x-|-x-|'.encode())
                num_sequencia = num_sequencia.decode()
                checksumm = checksumm.decode()

                dados_em_bits = ''.join([format(byte, '08b')for byte in dados])

                if checksumm == self.checksum(dados_em_bits):
                    print(f'pacote {int(num_sequencia[2:], 2)} recebido.')
                    arquivo_servidor.write(dados)
                else:
                    print(f'pacote {int(num_sequencia[2:], 2)} corrompido...')
                # gera uma execeção após um tempo de 2 segundos caso o receptor em questão não receba mais pacotes
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
        self.mesas = ['1','2','3','4','5','6','7','8','9','10']
        self.acoes = ['chefia','digite seu nome']
        self.nome_cliente = ''
        self.mesa_cliente = 0
        self.addr_cliente = ()

    def envia_pacote(self, socket, caminho_do_arquivo, ip_porta):
        arquivo = open(caminho_do_arquivo, 'rb')
        num_sequencia = 1

        while True:
            dados = arquivo.read(1024)
            dados_em_bits = ''.join([format(byte, '08b') for byte in dados])

            if not dados:
                break
            # Monta a mensagem com número de sequência, checksum e dados do pacote
            mensagem = f'{bin(num_sequencia)}|-x-|-x-|-x-|{self.checksum(dados_em_bits)}|-x-|-x-|-x-|'.encode()+dados
            # envia para o o socket (ip, porta)
            socket.sendto(mensagem, ip_porta)
            print(f'enviando pacote {num_sequencia}...')
            num_sequencia += 1
            time.sleep(0.0001)

        print('transmissão finalizada!')
        arquivo.close()

    def recebe_pacote(self, socket, caminho_do_arquivo):
        arquivo_servidor = open(caminho_do_arquivo, 'wb')
        # mensagem(recebe os dados do pacote), addr recebe a tupla (ip, porta),1024 representa o tamanho do pacote recebido
        mensagem, addr = socket.recvfrom(2048)
        socket.settimeout(0.05)

        try:
            while True:
                # Separa o número de sequência, o checksum e os dados do pacote
                num_sequencia, checksumm, dados = mensagem.split(
                    '|-x-|-x-|-x-|'.encode())
                num_sequencia = num_sequencia.decode()
                checksumm = checksumm.decode()
                # self.envia_ack(socket, mensagem,num_sequencia,addr)
                dados_em_bits = ''.join([format(byte, '08b')for byte in dados])

                if checksumm == self.checksum(dados_em_bits):
                    print(f'pacote {int(num_sequencia[2:], 2)} recebido.')
                    self.envia_ack(socket, mensagem, num_sequencia, addr)
                    print(f'- enviando ACK do pacote {int(num_sequencia[2:], 2)}...')
                    arquivo_servidor.write(dados)
                else:
                    print(f'pacote {int(num_sequencia[2:], 2)} corrompido...')
                # gera uma execeção após um tempo de 2 caso o o receptor em questão não receba mais pacotes
                # socket.settimeout(1)
                mensagem, addr = socket.recvfrom(2048)
        except TimeoutError:
            print('transmissão finalizada!')

        arquivo_servidor.close()


    def resposta_restaurante(self, socket, mensagem_cliente, addr_cliente):
        #mensagem, addr = socket.recvfrom(1024)
            # Separa o número de sequência, o checksum e os dados do pacote
        num_sequencia, checksumm, dados = mensagem_cliente.split('|-x--x-|'.encode())
        dados_em_bits = ''.join([format(byte, '08b')for byte in dados])

        
        if checksumm.decode() == self.checksum(dados_em_bits):
            print(f'pacote {int(num_sequencia[2:], 2)} recebido.')
            self.envia_ack(socket,dados.decode(),num_sequencia.decode(), addr_cliente )
            print(self.envia_ack(socket,dados.decode(),num_sequencia.decode(),addr_cliente ))
        else:
            print(f'pacote {int(num_sequencia[2:], 2)} corrompido...')
            return False
        # se o cliente fizer o chamadado para o restaurante, o restaurante pede um numero de mesa
        if dados.decode() == 'chefia':
            mensagem_resposta = 'CIntofome: digite sua mesa' 
            socket.sendto(mensagem_resposta.encode(), addr_cliente)

        # se o cliente responder com o seu numero de mesa, o restaurante salva sua mesa e pergunta seu nome
        elif dados.decode() in self.mesas:
            self.mesa_cliente = dados.decode()
            mensagem_resposta = 'CIntofome: digite seu nome' 
            socket.sendto(mensagem_resposta.encode(), addr_cliente)
           
        # se o cliente responde com o seu nome, o restaurante pergunta se o mesmo está só ou acompanhado
        elif dados.decode():
            self.nome_cliente = dados.decode()
            mensagem_resposta = 'CIntofome: Você está só ou acompanhado?'
            socket.sendto(mensagem_resposta.encode(), addr_cliente)
        # se o cliente não seguir o procedimento a opção é invalida.
        else:
            mensagem_resposta = 'opção invalida'
            socket.sendto(mensagem_resposta.encode(), addr_cliente)

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
