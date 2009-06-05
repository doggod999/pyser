#coding=utf-8
#Author: wzw6174
#Create time: 2009-06-04



import os
import config

from Tkinter import *
#from FileDialog import *

from BaseServer import BaseServer

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

#def button(root, side, text, command=None):
#    w = Button(root, text=text, command=command)
#    w.pack(side=side, expand=YES, fill=BOTH)
#    return w
 
def changePort():
    '''修改服务器端口'''
    MIN_PORT = 1024
    MAX_PORT = 65535
    new_port = 0
    tmp = port_input.get()
    if not cmp(tmp, ''):
        return 0
    
    try:
        new_port = int(tmp)
    except ValueError:
        listbox.insert(END, "非法字符")
        return 0

    if   new_port <= MIN_PORT or new_port >= MAX_PORT :
        listbox.insert(END, "端口范围必须在1024~65535之间!")
    
    else:
        config.PORT = new_port
        msg = '端口修改成功！现在的端口是', new_port
        listbox.insert(END, msg)
        listbox.insert(END, '请重启服务器...')
        
def changePath():
    '''修改服务器可访问资源的存放目录'''
#    fd = LoadFileDialog(root)
#    k = fd.go()
#    text1.delete(0, END)
#    text1.insert(END, k)
    path = path_input.get()
    if cmp(path, ''):
        if os.path.exists(path) and os.path.isdir(path):
            config.apppath = path
            listbox.insert(END, '资源目录修改成功！')
            listbox.insert(END, '请重启服务器...')
        else:
            listbox.insert(END, '路径不正确！')
            listbox.insert(END, '请确认您输入的路径存在！')
       
def startServer():
    pass 
def stopServer():
    pass
def showInfo():
    listbox.insert(END, '制作小组成员：欧必杰、吴志伟')   
    listbox.insert(END, '鸣谢：115、117') 
    listbox.insert(END, '版本号：1.0 Beta')  
def clear():
    listbox.delete(0, END)

root = Tk()   
root.title("服务器控制台")
root.geometry('350x250')

deyF = frame(root, TOP)
label1 = Label(deyF, text="端口:").pack(side=LEFT, expand=YES, fill=BOTH)
display = StringVar()
port_input = Entry(deyF, textvariable=display)
port_input.pack(side=LEFT, expand=YES, fill=BOTH)
port_change = Button(deyF, text="Change", command=changePort)
port_change.pack(side=LEFT, expand=YES, fill=BOTH)
   
opsF = frame(root, TOP)
label2 = Label(opsF, text="路径:") .pack(side=LEFT, expand=YES, fill=BOTH)
path_input = Entry(opsF)
path_input.pack(side=LEFT, expand=YES, fill=BOTH)
path_change = Button(opsF, text="Change", command=changePath)
path_change.pack(side=LEFT, expand=YES, fill=BOTH) 
   
wzwF = frame(root, TOP)
start_btn = Button(wzwF, text="启动", command=startServer)
start_btn.pack(side=LEFT, expand=YES, fill=BOTH)
stop_btn = Button(wzwF, text="停止", command=stopServer)
stop_btn.pack(side=LEFT, expand=YES, fill=BOTH)
clear_btn = Button(wzwF, text="清除", command=clear)
clear_btn.pack(side=LEFT, expand=YES, fill=BOTH)
about_btn = Button(wzwF, text="关于", command=showInfo)
about_btn.pack(side=LEFT, expand=YES, fill=BOTH)
quit_btn = Button(wzwF, text="退出", command=root.quit)
quit_btn.pack(side=LEFT, expand=YES, fill=BOTH)
 
clearF = frame(root, BOTTOM)
scrollbar = Scrollbar(clearF, orient=VERTICAL)
listbox = Listbox(clearF, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()