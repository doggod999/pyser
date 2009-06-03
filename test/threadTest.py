#coding=utf-8
import time, threading, socket

def handle_request(connect, client_addr):
    print 'New child', threading.currentThread().getName()
    print 'Got connection from', connect.getpeername()
    sleepPrint()
    while 1:
        data = connect.recv(4096)
        if not len(data):
            break
        connect.sendall(data)
    connect.close()
    
    
def sleepPrint():
    print 'sleeping...'
    time.sleep(10)
    print 'wake up...'
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8888))
s.listen(5)
while True:
    try:
        connect, client_addr = s.accept()
    except:
        traceback.print_exc()
        continue
        
    t = threading.Thread(target=handle_request, args=(connect, client_addr))
    #不必等所有线程结束
    t.setDaemon(1)
    t.start()
        
