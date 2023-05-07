import time

class Cliente ():
    def __init__(self) -> None:
        self.ip_porta = ('localhost', 3001)

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
        
    def recebe_solicitacao(self, socket):
        mensagem_cliente, addr_cliente = socket.recvfrom(1024)
        num_sequencia, checksumm, dados = mensagem_cliente.split('|-x--x-|'.encode())
        dados_em_bits = ''.join([format(byte, '08b')for byte in dados])

        if checksumm.decode() == self.checksum(dados_em_bits):
            print(f'pacote {int(num_sequencia[2:], 2)} recebido.')
            self.envia_ack(socket,dados.decode(),num_sequencia.decode(), addr_cliente )
            print(self.envia_ack(socket,dados.decode(),num_sequencia.decode(),addr_cliente ))
        else:
            print(f'pacote {int(num_sequencia[2:], 2)} corrompido...')

        return dados


    def resposta_restaurante(self, socket, dados, addr_cliente):
       
        # se o cliente fizer o chamadado para o restaurante, o restaurante pede um numero de mesa
        if dados.decode() == 'chefia':
            mensagem_resposta = 'CIntofome: digite sua mesa' 
            socket.sendto(mensagem_resposta.encode(), addr_cliente)

        # se o cliente responder com o seu numero de mesa, o restaurante salva sua mesa e pergunta seu nome
        elif dados.decode() in self.mesas:
            mensagem_resposta = 'CIntofome: digite seu nome' 
            socket.sendto(mensagem_resposta.encode(), addr_cliente)

           
        # se o cliente responde com o seu nome, o restaurante pergunta se o mesmo está só ou acompanhado
        elif dados.decode()[0:6] == 'nome: ':
            mensagem_resposta = 'opções: '
            socket.sendto(mensagem_resposta.encode(), addr_cliente)
        else:
            socket.sendto('comunicacao encerrada'.encode(), addr_cliente)

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
