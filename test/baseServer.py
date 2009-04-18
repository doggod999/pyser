import socket

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print 'Listening at port %s' % PORT
s.listen(5)

while True:
    try:
        connect, address = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    
    try:
        print connect.getpeername()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
        
    try:
        connect.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()