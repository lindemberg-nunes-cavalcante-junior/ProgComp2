import os,sys


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