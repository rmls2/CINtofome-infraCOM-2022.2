import socket
from modulo_auxiliar import Cliente, Servidor


# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_cliente.bind(Cliente().ip_porta)

input_cliente = input('digite 1 para envio de arquivo ou 2 para envio de mensagem: ')

match input_cliente:

    case '1':
        extensao_arquivo = input('digite a extensão do arquivo que será enviado: ')
        socket_cliente.sendto(extensao_arquivo.encode(), Servidor().ip_porta)

        caminho_do_arquivo = input('digite o caminho do arquivo: ')
        Cliente().envia_pacote(socket_cliente, caminho_do_arquivo, Servidor().ip_porta)

        print('\n**pacotes retransmitidos pelo servidor**\n')

        Cliente().recebe_pacote(socket_cliente,'./arqvs_cliente/arquivo_cliente'+extensao_arquivo)

    case '2':
        socket_cliente.sendto(''.encode(), Servidor().ip_porta)
        arquivo_cliente = open('./arqvs_cliente/arquivo_cliente', 'w')

        while True:
            mensagem_cliente = input('digite aqui sua mensagem: ')
            if mensagem_cliente == '\x18':
                break
            else:
                arquivo_cliente.write(f'{mensagem_cliente}\n')
        arquivo_cliente.close()

        Cliente().envia_pacote(socket_cliente,'./arqvs_cliente/arquivo_cliente', Servidor().ip_porta)

        print('\n**pacotes retransmitidos pelo servidor**\n')

        Cliente().recebe_pacote(socket_cliente, './arqvs_cliente/arquivo_cliente')
    #caso padrão: ação invalida.
    case _:
        print('opção invalida!')

socket_cliente.close()
