import time
import socket
from datetime import datetime
import random


def soma_numeros(probabilidade):
    count = 0
    for i in range(5):
        fator_de_probabilidade = random.random()
        print(fator_de_probabilidade)
        if fator_de_probabilidade < probabilidade:
            count += i
    return count


print(soma_numeros(0.9))


def gerador_de_perdas():
    pass


def envia_ack(socket, mensagem, num_seq, addr):
    if mensagem:
        ack = f'ACK {int(num_seq[2:], 2)}'
        socket.sendto(ack.encode(), addr)


def recebe_ack(socket, num_seq):
    if socket.recvfrom(512):
        print(f'ACK {num_seq} recebido')


start = datetime.now()
# seu código aqui
end = datetime.now()
time_taken = end - start
print('tempo de envio e recebimento de ack: {:.8f} segundos'.format(
    time_taken.total_seconds()))


# while True:
#     try:
#         if self.recebe_ack(socket):
#             break
#     except TimeoutError:
#         socket.sendto(mensagem, ip_porta)
#         print(f'\nreenviando pacote {num_sequencia}...')


# Defina o host e a porta do servidor
HOST = 'localhost'
PORT = 1234

# Defina a mensagem a ser enviada
mensagem = "Olá, servidor!"

# Defina o número máximo de reenvios
MAX_RESENDS = 3

# Defina o tempo limite para a resposta do servidor (em segundos)
TIMEOUT = 5

# Crie um soquete UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Defina o número de sequência inicial
num_sequencia = 0

# Enquanto o número de reenvios for menor que o máximo permitido
for i in range(MAX_RESENDS):

    # Envie o pacote e imprima a mensagem
    client_socket.sendto(mensagem.encode(), (HOST, PORT))
    print(f"\nEnviando pacote {num_sequencia}...")

    # Inicie o temporizador
    start_time = time.time()

    # Enquanto o tempo limite não for atingido
    while (time.time() - start_time) < TIMEOUT:

        # Aguarde a resposta do servidor
        try:
            client_socket.settimeout(TIMEOUT)
            ack, server_addr = client_socket.recvfrom(1024)
            if ack:
                print(
                    f"ACK recebido: {ack.decode()} do servidor {server_addr}")
                break
        except socket.timeout:
            print(f"Tempo limite atingido para o pacote {num_sequencia}!")

    # Se o ACK foi recebido, encerre o loop de reenvio e o programa
    # if ack:
        break

    # Se o tempo limite for atingido e o ACK não for recebido, reenvie o pacote
    print(
        f"ACK não recebido para o pacote {num_sequencia}. Tentando novamente...")

# Encerre o soquete e o programa
client_socket.close()
