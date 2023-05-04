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


from datetime import datetime
start = datetime.now()
# seu código aqui
end = datetime.now()
time_taken = end - start
print('tempo de envio e recebimento de ack: {:.8f} segundos'.format(time_taken.total_seconds()))



# while True:
#     try: 
#         if self.recebe_ack(socket):
#             break
#     except TimeoutError:
#         socket.sendto(mensagem, ip_porta)
#         print(f'\nreenviando pacote {num_sequencia}...')