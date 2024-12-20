import socket,sys,requests,os

dir = os.path.dirname(os.path.abspath(__file__))
try:
    arqentrada = open(dir + '\\Teste_de_Portas.txt','r')
    # lista = list(i[:-1].split(';')[0] if i[-1:] == '\n' else i.split(';')[0] for i in arqentrada)
except:
    print(f'{sys.exc_info()[0]}')

# Pegar o ip do host
host = input('Digite a URL:')

try:
    ip_host = socket.gethostbyname(host)
except:
    print('Não foi possível encontrar a url...')

Status = list()
porta = 80
while True:
    server_conn = (ip_host,porta)
    try:
        socket_teste = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket_teste.type)
        socket_teste.settimeout(2)
        socket_teste.connect(server_conn)
    except:
        Status.append({porta:{'porta':porta,'protocolo':socket.getservbyport(porta),'status':socket.error}})
        print(Status)
        break
    else:
        Status.append({porta:{'porta':porta,'protocolo':socket.getservbyport(porta),'status':'OK'}})
        break
