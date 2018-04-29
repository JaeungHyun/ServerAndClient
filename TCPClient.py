import socket

host = ''
port = 8080
ADDR = (host, port)

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect(ADDR)

Nums = input('Input equation: ')
Client.send(Nums.encode())

result = Client.recv(1024).decode()
print('Result: ', result)

Client.close()
