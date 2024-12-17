import socket,sys

host = input('Digite a URL:')

try:
    ip_host = socket.gethostbyname(host)
except:
    print('Não foi possível...')
else:
    print(ip_host)

server_conn = (ip_host,22)
socket_teste = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TimeoutError(5)

try:
    socket_teste.connect(server_conn)
except:
    print('error...')
