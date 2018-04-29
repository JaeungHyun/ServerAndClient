from socket import *

client = socket(AF_INET, SOCK_DGRAM)
equation = input('Input equation: ')
client.sendto(equation.encode(), ('localhost', 5001))

result, addr = client.recvfrom(1024)
print('Result: ', result)

client.close()
