import socket
from modulo_auxiliar import Cliente, Servidor

HOST = 'localhost'  # ip do servidor
PORT = 5030  # porta onde o servidor vai receber os pacotes
dest = (HOST, PORT)

# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_cliente.bind(Cliente().IP_PORTA_cliente)

if Cliente().inicia:
    entrada = input(
        'digite 1 para envio de arquivo ou 2 para envio de mensagem: ')

    match entrada:

        case '1':
            caminho_do_arquivo = input('digite o caminho do arquivo: ')
            Cliente().envia_pacote(socket_cliente, caminho_do_arquivo, Servidor().IP_PORTA_servidor)
            print('\n**pacotes retransmitidos**\n')
            Cliente().recebe_pacote(socket_cliente, './arqvs_cliente/arquivo_cliente')

        case '2':
            arquivo_cliente = open('./arqvs_cliente/arquivo_cliente', 'w')

            while True:
                mensagem_cliente = input('digite aqui sua mensagem: ')
                if mensagem_cliente == '\x18':
                    break
                else:
                    arquivo_cliente.write(f'{mensagem_cliente}\n')
            arquivo_cliente.close()

            Cliente().envia_pacote(socket_cliente,
                                   './arqvs_cliente/arquivo_cliente', Servidor().IP_PORTA_servidor)
            print('\n**pacotes retransmitidos**\n')
            Cliente().recebe_pacote(socket_cliente, './arqvs_servidor/arquivo_servidor')
        # caso padrão: ação invalida.
        case _:
            print('opção invalida!')

socket_cliente.close()
