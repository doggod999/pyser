#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-19

import socket

import config
import log

class BaseServer():
    def __init__(self):
        self.host = config.HOST
        self.port = config.PORT
        self.logger = log.Log()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((config.HOST, config.PORT))
        self.socket.listen(5)
        self.logger.info('Server start up successfully.\n')
        while True:
            self.handle_request()
        
    def handle_request(self):
        connect, client_addr = self.socket.accept()
        client_host = client_addr[0]
        print socket.getfqdn(client_host)

if __name__ == '__main__':
    BaseServer()