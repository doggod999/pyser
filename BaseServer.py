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
        self.run_server()
        
    def run_server(self):
        self.logger = log.Log()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((config.HOST, config.PORT))
        self.socket.listen(5)
        self.logger.info('Server start up successfully on port %d...\r\n' % config.PORT)
        while True:
            try:
                connect, client_addr = self.socket.accept()
            except:
                traceback.print_exc()
                continue
        
            t = threading.Thread(target=self.handle_request, args=(connect, client_addr))
            #主程序不必等所有线程结束
            t.setDaemon(1)
            t.start()
        
    def handle_request(self, connect, client_addr):
        '''处理请求'''
        
        #多线程测试
        print 'New child thread:', threading.currentThread().getName()
        self.sleepPrint()
        
        #得到客户端的ip以及主机名
        client_ip = client_addr[0]
        client_name = socket.getfqdn(client_ip)
        
        request = connect.recv(4096)
        http_response = HttpResponse.HttpResponse(connect)
        http_request = HttpRequest.HttpRequest(request)
        
        log_msg = '[%s] - - "%s"' % (client_name, http_request.request_dict['request_line'])
        
        if http_request.request_dict['method'] == 'GET':
            self.doGET(http_request, http_response, log_msg)
        else:
            http_response.send_error(400, http_request.request_dict['method'])
            log_msg += ' 400\r\n'
            
            lock.acquire()
            self.logger.info(log_msg)
            lock.release()
            
        connect.close()
        
    def doGET(self, http_request, http_response, log_msg):
        file = http_response.get_file(http_request.request_dict['url'], config.apppath)
        if file is None:
            http_response.send_error(404, http_request.request_dict['url'])
            log_msg += ' 404\r\n'
            
            lock.acquire()
            self.logger.info(log_msg)
            lock.release()
            
        else:
            f = open(file, 'rb')
            body = f.read()
            http_response.send_response(200, body)
            log_msg += ' 200\r\n'
            
            lock.acquire()
            self.logger.info(log_msg)
            lock.release()
            
    def sleepPrint(self):
        print 'sleeping...'
        time.sleep(10)
        print 'wake up!!!\n'

if __name__ == '__main__':
    BaseServer()