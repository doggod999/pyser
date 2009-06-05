#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-17

import os
import datetime

workpath = os.path.dirname(__file__)

#资源根目录
apppath = workpath + os.sep + 'webapps'

#日志文件保存文件夹
logpath = workpath + os.sep + 'logs'
#logfile = logpath + os.sep + get_log_filename()

#服务器的端口与地址
PORT = 8888
HOST = ''

if __name__ == '__main__':
    print 'workpath:', workpath
    print 'app path:', apppath
#    print 'log file:', logfile
    print 'port:', PORT
    print 'host:', HOST