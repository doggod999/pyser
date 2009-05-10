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
