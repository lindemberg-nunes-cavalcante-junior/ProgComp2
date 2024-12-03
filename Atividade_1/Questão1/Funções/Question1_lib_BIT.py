def ip2bin(Rede:str):
    Rede = Rede.split('.')
    for i in Rede:
        x = int.to_bytes(int(i),byteorder='big')
        print(bin(int.from_bytes(x,'big'))[2:])
    return
































'''def ip2bin(ipdecimal:str):
    ipdecimal = ipdecimal.split('.')

    # Validação
    if not isinstance(ipdecimal,str):
        raise ValueError
    if len(ipdecimal) != 4:
        raise Exception('Não possui 4 Octetos ou separação incorreta...')
    for i in ipdecimal:
        if i.isdigit() == False or int(i) < 0 or int(i) > 255:
            raise Exception('Range de tamanho Errado ou Formatação Errada...')
    if not isinstance(ipdecimal,str):
        raise ValueError
    # Conversão
    ipbinario = list(str(bin(int(x))[2:]) if len(str(bin(int(x))[2:]))==8 else ((8 - len(str(bin(int(x))[2:]))) *'0') + str(bin(int(x))[2:]) for x in ipdecimal)
    ipdecimal = ".".join(ipdecimal)
    ipbinario = ".".join(ipbinario)
    
    return ipdecimal,ipbinario

def cidr2mascara(cidrMascara:int):

    # Validação
    if not isinstance(cidr2mascara,int):
        raise Exception('Informe um valor inteiro...')
    elif  cidrMascara <0 or cidrMascara > 32:
        raise Exception('A máscara dada não é um positivo ou não está de acordo com o range de 0 a 32...')

    #Gerar Máscara em Binário
    strMascaraBin = list()
    Octeto = ''
    Tamanho = 4
    tipo = cidrMascara
    while Tamanho > 0:

        if tipo > 0:
            if tipo < 8:
                Octeto = '1'*tipo + '0'*(8 - tipo)
                tipo = 0
            elif tipo >= 8:
                Octeto = '1'*8
                tipo -= 8
        else:
            Octeto = '0'*8
        strMascaraBin.append(Octeto)
        Octeto = ''
        Tamanho -= 1
    
    #Mascara em Decimal
    strMascaraDec = list(str(int(x,2)) for x in strMascaraBin)

    strMascaraBin = ".".join(strMascaraBin)
    strMascaraDec = ".".join(strMascaraDec)
            

    return cidrMascara,strMascaraDec,strMascaraBin

def bit2bitAnd(strIpBin:str,strIpMascaraBin:str):

    #Validar
    if not isinstance(strIpBin, str) or not isinstance(strIpMascaraBin, str):
        raise ValueError
    if len(strIpBin.split('.')) != 4 or len(strIpMascaraBin.split('.')) != 4:
        raise Exception('Mascara ou Ip não possui 4 octetos...')
    for i in strIpBin.split('.'):
        if len(i) != 8:
            raise Exception('Ip de rede não possui todos os bytes...')
        for x in i:
            if x != '1' and x != '0':
                raise Exception('Octeto(s) errado...')
    for i in strIpMascaraBin.split('.'):
        if len(i) != 8:
            raise Exception('Ip da mascara não possui todos os bytes...')
        for x in i:
            if x != '1' and x != '0':
                raise Exception('Octeto(s) errado...')
    
    #Ip de Saída
    IpBinario = list(map(lambda x,i: i if x == i else '0'  ,strIpBin,strIpMascaraBin))
    IpBinario = "".join(IpBinario)
    
    return IpBinario

def bin2ip(bin:str):
    bin = bin.split('.')
    bin = list(str(int(x,2)) for x in bin)
    bin = ".".join(bin)
    return bin

def NetworkAdress(ip:str,Mask:str):
    Network = list(map(lambda x,i: x if x == i else '0'  ,ip,Mask))
    Network = "".join(Network)
    return Network

def Hosts(Rede:str,Masc:str,Bits:int):
    Fhost = Rede[:-1]
    Fhost = Fhost + '1'
    Broadcast = list(map(lambda x,i:'1' if x==i=='0' else x,Rede,Masc))
    Broadcast = "".join(Broadcast)
    Lhost = Broadcast[:-1]
    Lhost = Lhost + '0'
    Hosts = 2**(32 -Bits) - 2

    Fhost = bin2ip(Fhost)
    Broadcast = bin2ip(Broadcast)
    Lhost = bin2ip(Lhost)
    return Fhost,Broadcast,Lhost, Hosts'''