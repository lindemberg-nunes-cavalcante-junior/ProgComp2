import os,sys

class bcolor:
    verde = '\033[92m'
    amarelo = '\033[93m'
    cinza = '\033[90m'

def leituraArquivo():
    try:
        dirname = os.path.dirname(os.path.abspath(__file__))
        arquivo = open(dirname + '\\Palavras.txt','r',encoding='utf-8')
        palavras = list()
        for i in arquivo:
            i = i.replace('\n','')
            palavras.append(i)
           
        arquivo.close()
    except:
        raise Exception(f'ERROR:...{sys.exc_info()[0]}')
    else:
        return palavras