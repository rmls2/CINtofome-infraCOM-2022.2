# o código abaixo consegue abrir um arquivo ler seus bytes, transformá-lo em uma seq. de numero de 16 bits
# e depois somá-los e isso em teoria geraria o checksum de um numero.
import sys
arquivo = open('./arqvs/linkedin2.jpg', 'rb')

# print(arquivo.readlines()) # readlines gera uma lista com todas as linhas do arquivo

# for line in arquivo.readlines():
# print(line)

# código em list comprehension
# bytes = arquivo.read(2).decode()
# bytes_as_bits = ''.join(format(ord(byte), '08b') for byte in bytes)

# código em formato normal
bytes = arquivo.read(16)
print(type(bytes))
bytes_as_bits = ''
for byte in bytes:
    # cada byte será escrito com 8 bits, por isso '08b'
    byte_as_bit = format(byte, '08b')  # string de byte
    bytes_as_bits += byte_as_bit  # é uma string formada pelos bytes lidos do arquivo

bits = bytes_as_bits   # Substitua pela string de bits gerada a partir dos bytes

# retorna o tamanho em bytes da variavel bits
tamanho_em_bytes = sys.getsizeof(bits)
# retorna o tamanho em bytes da variavel bytes
tamanho_pacote = sys.getsizeof(bytes)
# print('o tamanho em bytes dos bytes concatenados: ', tamanho_em_bytes)
# print('o tamanho em bytes dos bytes concatenados: ', tamanho_pacote)
# print(type(tamanho_em_bytes))  # o tipo é um inteiro
# print(type(tamanho_pacote))

# Divide a string de bits em grupos de 16 caracteres
groups = [bits[i:i+16] for i in range(0, len(bits), 16)]

# Transforma cada elemento de groups (que é um uma string de binarios) em numeros inteiros
binaries = [int(group, 2) for group in groups]

# Soma os números inteiros que representam os binários em groups
soma = sum(binaries)


# Imprime os resultados
print('Grupos de 16 caracteres: ', groups)
print('Números binários convertidos para int: ', binaries)
# retorna a soma em binario que é uma string
print('Soma dos números binários: ', bin(soma))
# retorna a soma em binário que é uma string mas sem o '0b'
print('Soma dos números binários sem o "0b": ', bin(soma)[2:])
# retorna a soma em inteiro
print('Soma dos números binários em inteiros: ', soma)

tamanho_soma = sys.getsizeof(bin(soma))
print(tamanho_soma)

arquivo.close()


def checksum(dados):

    groups = [dados[i:i+16] for i in range(0, len(dados), 16)]
    binaries = [int(group, 2) for group in groups]
    soma_dados = sum(binaries)

    return bin(soma_dados)[2:]


print('essa é a função checksum: ', checksum(bits))


""" with open('./arqvs/linkedin2.jpg', 'rb') as arquivo:
    bytes = arquivo.read(1024)
    bytes_as_bits = ''
    for byte in bytes:
        byte_as_bit = format(byte, '08b')
        bytes_as_bits += byte_as_bit

    bits = bytes_as_bits   # Substitua pela string de bits gerada a partir dos bytes

    # Divide a string de bits em grupos de 16 caracteres
    groups = [bits[i:i+16] for i in range(0, len(bits), 16)]

    # Transforma cada grupo em um número binário
    binaries = [int(group, 2) for group in groups]

    # Soma os números binários
    soma = sum(binaries)

    # Imprime os resultados
    print('Grupos de 16 caracteres: ', groups)
    print('Números binários: ', binaries)
    print('Soma dos números binários: ', bin(soma)) """

if 10:
    pass