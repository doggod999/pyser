import socket

msg = '''GET / HTTP/1.1
Host: www.baidu.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: gb2312,utf-8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive'''

if __name__ == '__main__': 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('www.baidu.com', 80))
    sock.send(msg)
    print sock.recv(1024)
    print sock.recv(1024)
    print sock.recv(1024)
    print sock.recv(1024)
    sock.close()