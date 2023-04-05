# Projeto CINtofome

![Em desenvolvimento](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![data da ultima atualizaçao](https://img.shields.io/badge/data%20da%20%C3%BAltima%20vers%C3%A3o-abril-green)
![branches](https://img.shields.io/badge/branches-1-orange)
 
 #### _obs: a descrição e demais explicações do projeto dizem respeito, por enquanto, a primeira parte do projeto CINtofome_

## Índice 

* [Descrição](#descrição)
* [Como funciona](#como-funciona)
* [Instruções para rodar o projeto](#instruções-para-rodar-o-projeto)
* [Desenvolvedores](#desenvolvedores)

## Descrição

Projeto realizado na disciplina de Infraestrutura de Comunicação do período de 2022.2. O objetivo da primeira parte é usar a interface de socket, através modulo Socket.py, para implementar uma comunicação com trasferência de arquivo entre cliente e servidor.

## Como funciona 

Usando o módulo socket.py implementamos a comunicação entre  scripts diferentes que representam um cliente e  um servidor. Os scripts se comunicam entre si, como também enviam arquivos de áudio, imagem, vídeo, etc. O script do cliente é capaz de mandar esses dados e o script do servidor é capaz de armazená-los e retransmití-los de volta ao cliente, como acontece no modelo cliente-servidor entre aplicações as aplicações de rede.  

## Instruções para rodar o projeto 

Após fazer o clone do repositório na sua máquina, abra-o usando o VScode. Exiba um terminal e faça um split da janela, ou abra dois terminais, para visualizar o que está acontecendo no script do cliente e no do servidor. Execute o script _servidor.py_, conforme mostrado abaixo: 

```bash
python3 servidor.py
```
Assim que o script do servidor for executado, o trminal exibirá uma pergunta sobre o tipo de pacote que o cliente quer enviar ao o servidor. Se for uma comunicação por mensagem a opção digitada tem que ser _mensagem_, se for transferência de arquivo o input precisa ser _arquivo_

```bash
Que tipo de pacote você deseja receber, mensagem ou arquivo?
Digite sua opção: 
```
Agora, execute o script _cliente.py_ para enviar os pacotes ao servidor. 

```bash
python3 cliente.py
```
assim que o script do cliente for executado, o terminal vai exibir a seguinte mensagem

```bash
Deseja mandar uma mensagem? (y/n):  
```

a resposta _y_ ou _n_ (sim ou não) vai depender do que o cliente quer enviar para o servidor. Se ao rodar o script do servidor, decidimos por envio de arquivo, o input a ser colocado precisa ser _n_ ou seja, *não*. 

```bash
deseja mandar uma mensagem para o servidor? (y/n): n
```
Dessa forma, o terminal exibirá a seguinte mensagem:

```bash
então você deseja enviar um arquivo para o servidor? (y/n):
```

Nessa parte, devemos dar o input _y_ e o terminal irá exibir a seguinte mensagem

```bash
passe o caminho do arquivo:
```
Na pasta *arqvs* há alguns arquivos para teste utilizando as extensões requeridas para a primeira parte do projeto. Nesse caso, para enviar um arquivo dessa pasta basta digitarmos ` ./arqvs/nome-do-arquivo ` . 
para exemplificar, vamos utilizar o arquivo _linkedin2.kpg_ e vamos enviá-lo para o servidor.

```bash
passe o caminho do arquivo aqui:./arqvs/linkedin2.jpg
```
após isso, o script do cliente vai enviar o arquivo _linkedin2.kpg_ para o servidor. O servidor por sua vez vai armazenar os pacotes na variável _arquivo_ que foi o nosso input inicial quando inicializamos o servidor. Após isso, o servidor vai retransmitir esses dados de volta ao cliente.
Quando todas essas etapas forem finalizadas os scripts irão exibir as seguintes mensagens

_servidor.py_
```bash
arquivo retransmitido ao cliente com sucesso!
```
_cliente.py_
```bash
arquivo recebido com sucesso
```


## Desenvolvedores

|  [<img src="https://avatars.githubusercontent.com/u/93690581?v=4" width=115><br><sub>Robbert Miller</sub>](https://github.com/rmls2) | [<img src="https://avatars.githubusercontent.com/u/47424471?v=4" width=115><br><sub>Filipe Fernando</sub>](https://github.com/lipe-1512) |
| :---: | :---: 


