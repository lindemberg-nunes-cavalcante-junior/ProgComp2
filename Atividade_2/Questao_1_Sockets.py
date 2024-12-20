import socket,sys,os,json

dir = os.path.dirname(os.path.abspath(__file__))
try:
    arqentrada = open(dir + '\\Teste_de_Portas.txt','r')
    arqentrada.readline()
except:
    print(f'{sys.exc_info()[0]}')

# Pegar o ip do host
host = input('Digite a URL:')

try:
    ip_host = socket.gethostbyname(host)
except:
    print('Não foi possível encontrar a url...')

# Teste das portas
Status = list()
while True:
    porta = arqentrada.readline()
    if porta[-1:] == '\n': porta = porta[:-1]
    elif porta == '':
        arqentrada.close()
        socket_teste.close()
        break
    porta = porta.split(';')
    
    server_conn = (ip_host,int(porta[0]))

    try:
        print(f'Testando....{ip_host} - {porta[0]}')
        socket_teste = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_teste.settimeout(2)
        socket_teste.connect(server_conn)
    except:
        Status.append({int(porta[0]):{'porta':int(porta[0]),'protocolo':porta[1] + '-' + porta[2],'status':socket.error}})
    else:
        Status.append({int(porta[0]):{'porta':int(porta[0]),'protocolo':porta[1] + '-' + porta[2],'status':'OK'}})


arqsaida = open(dir + '\\Teste_de_Portas.json','w')
json.dump(Status,arqsaida)
    

