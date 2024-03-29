#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-19

import socket
import time
import threading

import config
import log
import HttpRequest, HttpResponse

lock = threading.RLock()

class BaseServer():
    def __init__(self):
        self.host = config.HOST
        self.port = config.PORT
#        self.run_server()
    
    def stopServer(self):
        '''停止服务器'''
        msg = '''HEAD / HTTP/1.1'''
        if not self.is_running:
            return
        self.is_running = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if cmp(self.host, ''):
            sock.connect((self.host, self.port))
        else:
            sock.connect(('localhost', self.port))
        sock.send(msg)
        for i in range(10):
            sock.recv(1024)
        sock.close()
        self.logInfo('Server stop successfully!\r\n')
        
    def runServer(self):
        '''启动服务器'''
        self.is_running = True
        self.host = config.HOST
        self.port = config.PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.logInfo('Server start up successfully on port %d...\r\n' % self.port)
        while self.is_running:
            try:
                connect, client_addr = self.socket.accept()
            except:
                traceback.print_exc()
                continue
        
            t = threading.Thread(target=self.handleRequest, args=(connect, client_addr))
            #主程序不必等所有线程结束
            t.setDaemon(1)
            t.start()
        
    def handleRequest(self, connect, client_addr):
        '''处理请求'''
        
        #多线程测试
#        print 'New child thread:', threading.currentThread().getName()
#        self.sleepPrint()
        
        #得到客户端的ip以及主机名
        client_ip = client_addr[0]
        client_name = socket.getfqdn(client_ip)
        
        request = connect.recv(4096)
        http_response = HttpResponse.HttpResponse(connect)
        try:
            http_request = HttpRequest.HttpRequest(request)
        except:
            http_response.sendError(400)
            log_msg = '[%s] - - bad request\r\n' % (client_name)
            self.logInfo(log_msg)
            connect.close()
            return
        
        log_msg = '[%s] - - "%s"' % (client_name, http_request.request_dict['request_line'])
        
        if http_request.request_dict['method'] == 'GET':
            self.doGET(http_request, http_response, log_msg)
        elif http_request.request_dict['method'] == 'POST':
            self.doPOST(http_request, http_response, log_msg)
        elif http_request.request_dict['method'] == 'HEAD':
            self.doHEAD(http_request, http_response, log_msg)
        else:
            http_response.sendError(400)
            log_msg += ' 400\r\n'
            self.logInfo(log_msg)
        connect.close()
        
    def doGET(self, http_request, http_response, log_msg):
        '''响应get方法'''
        flag = http_response.doGetResponse(http_request.request_dict['url'], config.apppath)
        if flag == False :
            log_msg += ' 404\r\n'
            self.logInfo(log_msg)
        else:
            log_msg += ' 200\r\n'
            self.logInfo(log_msg)
    
    def doPOST(self, http_request, http_response, log_msg):
        '''响应post方法'''
        flag = http_response.doPostResponse(http_request.request_dict['url'], config.apppath)
        if flag == False :
            log_msg += ' 404\r\n'
            self.logInfo(log_msg)
        else:
            log_msg += ' 200\r\n'
            self.logInfo(log_msg)
            
    def doHEAD(self, http_request, http_response, log_msg):
        '''响应head方法'''
        flag = http_response.doHeadResponse(http_request.request_dict['url'], config.apppath)
        if flag == False :
            log_msg += ' 404\r\n'
            self.logInfo(log_msg)
        else:
            log_msg += ' 200\r\n'
            self.logInfo(log_msg)
        
    def logInfo(self, log_msg):  
        logger = log.Log() 
        lock.acquire()
        logger.info(log_msg)
        lock.release() 
        
    def logWarning(self, log_msg): 
        logger = log.Log() 
        lock.acquire()
        logger.warning(log_msg)
        lock.release() 
        
    def logError(self, log_msg):  
        logger = log.Log()
        lock.acquire()
        logger.error(log_msg)
        lock.release() 
        
    def sleepPrint(self):
        print 'sleeping...'
        time.sleep(10)
        print 'wake up!!!\n'

if __name__ == '__main__':
    b = BaseServer()
    b.runServer()