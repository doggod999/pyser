#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-18

import os
import datetime

import config

class Log():
    """ 系统日志 """
    def __init__(self):
        if not os.path.exists(config.logpath):
            os.makedirs(config.logpath)
        self.file = open(config.logfile, 'ab')
    
    def write(self, msg):
        self.file.writelines(msg)
        self.file.flush()
        
    def info(self, msg):
        msg = self.get_time() + ' -- INFO -- ' + msg
        self.write(msg)
        
    def error(self, msg):
        msg = self.get_time() + ' -- ERROR -- ' + msg
        self.write(msg)
        
    def warning(self, msg):
        msg = self.get_time() + ' -- WARNING -- ' + msg
        self.write(msg)
        
    def get_time(self):
        return datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        
    def __del__(self):
        self.file.close()
        
        
if __name__ == '__main__':
    logger = Log()
    logger.info('test111111\n')
    logger.error('test22222222\n')
    logger.warning('test33333333\n')
    logger.__del__()
        