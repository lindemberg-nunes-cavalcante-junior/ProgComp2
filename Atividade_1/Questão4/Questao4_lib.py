import os

def xor(origem:str,chave:str,destino:str):
    origem = list(origem.encode('ascii'))
    chave = list(chave.encode('ascii'))
    print(len(chave))
    contador = 1

    dirname = os.path.dirname(os.path.abspath(__file__))
    arquivo = open(dirname + f'\\{destino}','w',encoding='utf-8')
    palavra = bytes([])

    for i in origem:
        escrever = i^chave[contador-1]
        escrever = int(escrever).to_bytes(1,'big')
        palavra += escrever
        if contador == len(chave):
            contador = 1
        else: contador += 1
    
    arquivo.write(f'{palavra}')
    arquivo.close()
    
    return 'ok'