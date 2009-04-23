#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-17

import os
import datetime

def get_log_filename():
    return datetime.datetime.now().strftime('Server.%Y-%m-%d.log')

workpath = os.path.dirname(__file__)
apppath = workpath + os.sep + 'webapps'
logpath = workpath + os.sep + 'logs'
logfile = logpath + os.sep + get_log_filename()

#服务器的端口
PORT = 8888
HOST = ''

if __name__ == '__main__':
    print 'workpath:', workpath
    print 'app path:', apppath
    print 'log file:', logfile
    print 'port:', PORT