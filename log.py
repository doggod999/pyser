#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-18

import os, sys
import datetime

try:
    import config
except ImportError:
    print 'Can\'t find config file!'
    sys.exit(0)
    
class Log():
    """ 系统日志 """
    def __init__(self):
        self.logpath = config.logpath
        self.logfile = config.logfile
        if not os.path.exists(self.logpath):
            os.makedirs(self.logpath)
    
    #将msg写入log文件并打印到控制台
    def write(self, msg):
        self.file = open(self.logfile, 'ab')
        self.file.writelines(msg)
        self.file.flush()
        self.file.close()
        print msg
        
    def info(self, msg):
        msg = self.get_time() + ' - - INFO - - ' + msg
        self.write(msg)
        
    def error(self, msg):
        msg = self.get_time() + ' - - ERROR - - ' + msg
        self.write(msg)
        
    def warning(self, msg):
        msg = self.get_time() + ' - - WARNING - - ' + msg
        self.write(msg)
        
    def get_time(self):
        return datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        
if __name__ == '__main__':
    logger = Log()
    logger.info('test111111\n')
    logger.error('test22222222\n')
    logger.warning('test33333333\n')