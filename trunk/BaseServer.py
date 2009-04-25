#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-19

import socket

import config
import log
import HttpRequest, HttpResponse

class BaseServer():
    def __init__(self):
        self.logger = log.Log()
        self.run_server()
        
    def run_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((config.HOST, config.PORT))
        self.socket.listen(5)
        self.logger.info('Server start up successfully on port %d...\r\n' % config.PORT)
        while True:
            self.handle_request()
        
    def handle_request(self):
        connect, client_addr = self.socket.accept()
        self.http_response = HttpResponse.HttpResponse(connect)
        
        client_ip = client_addr[0]
        client_name = socket.getfqdn(client_ip)
        
        request = connect.recv(1024)
        self.http_request = HttpRequest.HttpRequest(request)
        
        self.log_msg = '[%s] - - "%s"' % (client_name, self.http_request.request_dict['request_line'])
        
        if self.http_request.request_dict['method'] == 'GET':
            self.doGET()
        else:
            self.http_response.send_error(400, self.http_request.request_dict['method'])
            self.log_msg += ' 400\r\n'
            self.logger.info(self.log_msg)
        connect.close()
        
    def doGET(self):
        file = self.http_response.get_file(self.http_request.request_dict['url'], config.apppath)
        if file is None:
            self.http_response.send_error(404, self.http_request.request_dict['url'])
            self.log_msg += ' 404\r\n'
            self.logger.info(self.log_msg)
        else:
            f = open(file, 'rb')
            body = f.read()
            self.http_response.send_response(200, body)
            self.log_msg += ' 200\r\n'
            self.logger.info(self.log_msg)

if __name__ == '__main__':
    BaseServer()