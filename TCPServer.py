import socket

host = ''
port_client = 8080


ClientADDR = (host, port_client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ClientADDR)
server.listen(5)


def Infix(expr):
    expr = list(expr)
    stack = list()
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if c in "0123456789.":
            num += c
        else:
            if num != "":
                stack.append(num)
                num = ""
            if c in "+-*/":
                stack.append(c)
            elif c == ")":
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                if op == "+":
                    stack.append(str(float(num1) + float(num2)))
                elif op == "-":
                    stack.append(str(float(num1) - float(num2)))
                elif op == "*":
                    stack.append(str(float(num1) * float(num2)))
                elif op == "/":
                    stack.append(str(float(num1) / float(num2)))
    return stack.pop()


print("Server is operating")


while 1:
    client, addr = server.accept()
    print('Client', addr)
    print('is connected.')

    result = Infix(client.recv(1024).decode())

    print('Result: ', result)

    client.send(result.encode())
    client.close()

    quit_server = input('If you want to stop server, input q : ')
    if quit_server == 'q':
        break

server.close()
