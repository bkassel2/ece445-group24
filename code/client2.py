import socket

ClientMultiSocket = socket.socket()
host = socket.gethostname()
port = 8080

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Hey there: ')
    if Input == 'q':
        break
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))


ClientMultiSocket.close()