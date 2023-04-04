# modulo criado para gerar uma interface amigavel no terminal para decidir se o cliente vai enviar mensage pura ou arquivo

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


def inicia_servidor():
    while True:
        entrada_servidor = input(
            'deseja mandar uma data_msg para o servidor? (y/n): ')

        if entrada_servidor == 'y' or entrada_servidor == 'Y':
            global data_msg
            data_msg = 'ok'  # input('digite sua data_msg aqui: ')
            return True
        elif entrada_servidor == 'n' or entrada_servidor == 'N':
            entrada_servidor = input(
                'então você deseja enviar um arquivo para o servidor? (y/n): ')
            if entrada_servidor == 'y' or entrada_servidor == 'Y':
                global arquivo
                arquivo = input('passe o caminho do arquivo aqui: ')
                return False
            else:
                print('resposta incorreta, vamos tentar novamente!\n')
                continue


""" if inicio():
    print('você digitou a data_msg: ', data_msg)
else:
    print('o caminho do seu arquivo é: ', arquivo) """
