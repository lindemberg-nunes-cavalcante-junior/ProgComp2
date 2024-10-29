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

#AddressIp = input('Digite seu Endereço de Ip(0.0.0.0): ')
#MaskI = int(input('Digite sua máscara de rede(0.0.0.0): '))
#MaskF = input('Digite sua máscara de rede final(0.0.0.0):')

AddressIp = '10.1.0.0'
MaskI = 8
MaskF = 10

Ips = []

for i in range(MaskI,MaskF + 1):
    cidr = i
    AddressIpBin = Question1_lib.ip2bin(AddressIp)

    MaskIp = Question1_lib.cidr2mascara(cidr)

    Ipsaida = Question1_lib.bit2bitAnd(AddressIpBin[1],MaskIp[2])

    SubMask = Question1_lib.bin2ip(Ipsaida)
    
    NetworkAdress = Question1_lib.NetworkAdress(AddressIpBin[1],Ipsaida)

    FirstHost = Question1_lib.FirstHost(NetworkAdress[0])
    print(FirstHost)
    Ips.append([cidr, NetworkAdress])



