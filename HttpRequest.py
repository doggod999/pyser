#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-23

class HttpRequest():
    def __init__(self, request):
        self.request_dict = {'request': request}
        self.parse_request()
        
    def parse_request(self):
        '''分析http请求'''
        
        request = self.request_dict['request']
        request = request.replace('\r', '')
        request_list = request.split('\n')
        self.request_dict['request_line'] = request_list[0]
        self.parse_request_line()
        
        print self.request_dict['request_line']
        print self.request_dict['method']
        print self.request_dict['url']
        print self.request_dict['version']
        
    def parse_request_line(self):
        '''分析http请求行'''
        
        request_line = self.request_dict['request_line']
        line_list = request_line.split(' ')
        self.request_dict['method'] = line_list[0]
        self.request_dict['url'] = line_list[1]
        self.request_dict['version'] = line_list[2]
        
    def pp(self):
        print self.request