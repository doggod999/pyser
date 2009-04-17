import socket

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print 'Listening at port %s' % PORT
s.listen(5)

while True:
    connect, address = s.accept()
    print connect.getpeername()
    connect.close()