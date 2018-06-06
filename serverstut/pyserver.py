import socket

PORT_NUMBER = 7760

def server_func():
    server = socket.socket()
    server.bind(('0.0.0.0', PORT_NUMBER))
    server.listen(1)
    client, address = server.accept()
    print 'Connection address:', address
    data = client.recv(1024)
    client.send("The data:" + data)
    client.close()
    server.close()


if __name__ == '__main__':
    server_func()