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

![img1](https://user-images.githubusercontent.com/93690581/229764005-c80ddb70-c192-42b1-87a4-3966f542acfa.png)

O script do servidor decidirá o tipo de pacote que ele irá receber, ou seja, se será apenas uma troca de mensagem ou envio de arquivo. Apesar de ser uma situação irreal, essa primeira implementação foi pensanda apenas para cumprir os requisitos da primeira parte do projeto (so... Easy, tiger!). 

Agora, execute o script _cliente.py_ e decida o pacote que o cliente irá mandar. Nesse caso, como nossa escolha é pré-definida, temos que mandar um pacote de acordo com o que foi definido no servidor. Para isso, precisamos mandar alguns inputs para o terminal conforme mostrado abaixo: 

![img2](https://user-images.githubusercontent.com/93690581/229767118-04f52099-a6b9-4339-9f83-42df65388092.png)

como podemos ver, ao executar _cliente.py_ a linha de comando nos dá algumas opções. Se quisermos enviar um pacote de mensagem - como se fosse um chat -  para o servidor digitamos 'y' para o primeiro input, caso contrário digitamos 'n' na CLI. A próxima linha exibirá uma pergunta sobre o envio de arquivo. Como queremos enviar um arquivo, então digitamos 'y' e passamos o caminho do arquivo que queremos enviar no próximo input. Após isso, precisamos definir um nome para o arquivo (*) que guardará os pacotes retransmitidos pelo servidor (ou seja, vamos definir um espaço para os dados que será retransmitido de volta ao cliente). Feita toda essa preparação, o cliente vai enviar o arquivo ao servidor.

![img3](https://user-images.githubusercontent.com/93690581/229774795-a2a31534-783e-4e8d-9c72-b4ded61f49b9.jpg)


Dessa forma, o servidor vai receber os dados que foram enviados pelo cliente e vai armazená-los em um novo arquivo. Logo após isso, o servidor vai retransmitir o arquivo que ele recebeu de volta ao cliente que vai salvá-los no arquivo (*).  

![img4](https://user-images.githubusercontent.com/93690581/229774840-ae0d3904-5374-47e3-a000-8089a5d3ab19.jpg)



## Desenvolvedores

|  [<img src="https://avatars.githubusercontent.com/u/93690581?v=4" width=115><br><sub>Robbert Miller</sub>](https://github.com/rmls2) | [<img src="https://avatars.githubusercontent.com/u/47424471?v=4" width=115><br><sub>Filipe Fernando</sub>](https://github.com/lipe-1512) |
| :---: | :---: 


