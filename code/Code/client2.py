import socket

HOST = socket.gethostname() # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket()
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
    command = input('Hey there: ')
    s.send(command.encode('utf-8'))
    reply = s.recv(1024)
    if reply == 'Terminate':
        break
    print (reply)