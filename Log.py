#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-18

class Log():
    def __init__(self, filename):
        self.file = open(filename, 'rw')
        