#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-23
import os

class HttpRequest():
    def __init__(self, request):
        self.request_dict = {'request': request}
        self.parse_request()
        
    def parse_request(self):
        '''分析http请求'''
        
        request = self.request_dict['request']
        print request
        request = request.replace('\r', '')
        request_list = request.split('\n')
        self.request_dict['request_line'] = request_list[0]
        self.parse_request_line()
        
        if self.request_dict['method'] == 'POST':
            self.request_dict['entity_body'] = request_list[-1]
            self.parse_entity_body()
        if self.request_dict['method'] == 'GET':
            temp_list = self.request_dict['url'].split('?')
            if len(temp_list) == 2:
                self.request_dict['url'] = temp_list[0]
                self.request_dict['entity_body'] = temp_list[1]
                self.parse_entity_body()
        pp = self.add_slash(self.request_dict['url'])
        print pp
        
    def parse_request_line(self):
        '''分析http请求行'''
        
        request_line = self.request_dict['request_line']
        line_list = request_line.split(' ')
        self.request_dict['method'] = line_list[0]
        self.request_dict['url'] = line_list[1]
        self.request_dict['version'] = line_list[2]
        
    def parse_entity_body(self):
        '''分析POST方法的请求实体'''
        
        pass
#        entity_body = self.request_dict['entity_body']

    def add_slash(self, url):
        '''解析要请求的url，末尾自动补全斜杠'''
        
        words = url.split('/')
        words = filter(None, words)
        path = '/'
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)
        if os.path.isdir(path):
            path = path + '/'
        return path
