import socket
from teste_mod_aux import Cliente, Servidor, load_data, save_data
import datetime
import json
# criação do socket do cliente, AF_INET representa o ipv4 e SOCK_DGRAM representa o socket udp
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# o bind vai alocar reserva de buffer para que a porta do cliente possa receber os dados passados a ela
socket_servidor.bind(Servidor().ip_porta)

print('***************************************************************')
print('**** CINto fome está aberto esperando receber clientes! :) ****')
print('***************************************************************')
print('***************************************************************')
# mensagem do servidor
horas = datetime.datetime.now().strftime('%H:%M')
mensagem_servidor = 'CIntofome: digite sua mesa'

cardapio = Servidor().cardapio()
informacoes_cliente = []
opcoes = Servidor().opcoes()

while True:

    dados = Servidor().recebe_solicitacao(socket_servidor)
    
    if dados.decode()[0:6] == 'nome: ':
        informacoes_cliente.append(dados.decode()[6:])
    if dados.decode() in Servidor().mesas:
        informacoes_cliente.append(dados.decode())
    print(informacoes_cliente)

    try:
        socket_servidor.settimeout(10)
        Servidor().resposta_restaurante(socket_servidor, dados, Cliente().ip_porta)
        if dados.decode()[:5] == 'nome:':
            break
       
    except TimeoutError:
        print('comunicação finalizada')
        break

informacoes_cliente.append(Cliente().ip_porta)
print('são esses os dados do cliente:' , informacoes_cliente)


# parte dois ter que apresentar o menu de opções para o cliente

dados = Servidor().recebe_solicitacao(socket_servidor)
dados = dados.decode()

if dados == '1' or dados == 'cardápio':
    with open('cardapio.json', 'w') as f:
        json.dump({}, f)
        print('json criado')

    data = load_data()
    data['cardapio'] = cardapio
    save_data(data)
    data_json = json.dumps(data, indent=4)
    socket_servidor.sendto(data_json.encode(), Cliente().ip_porta)

socket_servidor.close() 

