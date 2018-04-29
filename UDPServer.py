from socket import *


PORT = 5001

server = socket(AF_INET, SOCK_DGRAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('localhost', PORT))


print("Server is operating")


while 1:
    data, addr = server.recvfrom(1024).decode()
    print('Client', addr, 'is connected.')

    result = str(eval(data))     # eval로 계산
    print('Result: ', result)

    server.sendto(result.encode(), addr)

    quit_server = input()
    if quit_server == 'q':
        break

server.close()
