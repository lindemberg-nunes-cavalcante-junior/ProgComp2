def ip2bin(ipdecimal:str):
    ipdecimal = ipdecimal.split('.')

    # Validação
    if len(ipdecimal) != 4:
        raise Exception('Não possui 4 Octetos ou separação incorreta...')
    for i in ipdecimal:
        if i.isdigit() == False or int(i) < 0 or int(i) > 255:
            raise Exception('Range de tamanho Errado ou Formatação Errada...')
    # Conversão
    ipbinario = list(str(bin(int(x))[2:]) if len(str(bin(int(x))[2:]))==8 else ((8 - len(str(bin(int(x))[2:]))) *'0') + str(bin(int(x))[2:]) for x in ipdecimal)
    ipdecimal = ".".join(ipdecimal)
    print(ipdecimal)
    ipbinario = ".".join(ipbinario)
    print(ipbinario)
    return ipdecimal,ipbinario