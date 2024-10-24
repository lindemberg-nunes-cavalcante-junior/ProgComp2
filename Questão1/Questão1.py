'''
1. Implemente uma calculadora de sub-rede em Python. O programa deve solicitar um endereço IP, uma 
máscara de rede inicial e uma máscara de rede final. Para cada máscara de rede no intervalo 
especificado, o programa deve calcular e exibir as seguintes informações: 
a) Endereço de Rede 
b) Primeiro Host 
c) Último Host 
d) Endereço de Broadcast 
e) Máscara de Sub-rede em Decimal e Binário 
f) 
Número de Hosts Válidos. 
Requisitos: 
a) NÃO utilize a biblioteca ipaddress; 
b) Valide o endereço IP e as máscaras de rede fornecidas pelo usuário; 
c) Salve os resultados em um arquivo no formato JSON (dicionário). Não subscreva arquivos 
existentes; 
d) Formate as saídas de forma clara e organizada (se quiser pode usar a biblioteca tabulate). 
'''
from Funções import Question1_lib
import tabulate

AddressIp = input('Digite seu Endereço de Ip(0.0.0.0): ')
#MaskI = input('Digite sua máscara de rede(0.0.0.0): ')
#MaskF = input('Digite sua máscara de rede final(0.0.0.0):')

AddressIpBin = Question1_lib.ip2bin(AddressIp)




