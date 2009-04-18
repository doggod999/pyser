#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-19

import config

class BaseServer():
    def __init__(self):
        self.host = config.HOST
        self.port = config.PORT
        

if __name__ == '__main__':
    bs = BaseServer()
    print bs.host
    print bs.port