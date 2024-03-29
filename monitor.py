#coding=utf-8
#Author: wzw6174
#Create time: 2009-06-04

import os
import config
import threading

from Tkinter import *
#from FileDialog import *

from BaseServer import BaseServer

server = BaseServer()
server_thread = threading.Thread()

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

#def button(root, side, text, command=None):
#    w = Button(root, text=text, command=command)
#    w.pack(side=side, expand=YES, fill=BOTH)
#    return w
 
def change_port():
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
        msg = '端口修改成功！重启后端口将改为', new_port
        listbox.insert(END, msg)
        listbox.insert(END, '请重启服务器...')
        
def change_path():
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
       
def start_server():
    '''启动服务器'''
    global server_thread 
    if not server_thread.isAlive():
        server_thread = threading.Thread(target=server.runServer)
        server_thread.setDaemon(1)
        server_thread.start()
        listbox.insert(END, 'HTTP服务成功启动！') 
    else:
        listbox.insert(END, 'HTTP服务已启动！') 

def stop_server():
    '''停止服务器'''
    global server_thread 
    if server_thread.isAlive():
        server.stopServer()
        listbox.insert(END, 'HTTP服务成功停止！') 
    else:
        listbox.insert(END, 'HTTP服务已停止！') 
        
def show_info():
    '''显示帮助'''
    listbox.insert(END, '服务器版本：1.0')
    listbox.insert(END, '学生：ooaixt、wzw')   
    listbox.insert(END, '联系方式：doggod999@gmail.com、wzw6174@gmail.com') 
      
    
def clear():
    '''清除文本显示'''
    listbox.delete(0, END)
    
def quit():
    stop_server()
    root.quit()

root = Tk()   
root.title("服务器控制台")
root.geometry('350x250')

#端口输入框及按钮
deyF = frame(root, TOP)
label1 = Label(deyF, text="端口:").pack(side=LEFT, expand=YES, fill=BOTH)
display = StringVar()
port_input = Entry(deyF, textvariable=display)
port_input.pack(side=LEFT, expand=YES, fill=BOTH)
port_change = Button(deyF, text="Change", command=change_port)
port_change.pack(side=LEFT, expand=YES, fill=BOTH)

#资源路径输入框及按钮
opsF = frame(root, TOP)
label2 = Label(opsF, text="路径:") .pack(side=LEFT, expand=YES, fill=BOTH)
path_input = Entry(opsF)
path_input.pack(side=LEFT, expand=YES, fill=BOTH)
path_change = Button(opsF, text="Change", command=change_path)
path_change.pack(side=LEFT, expand=YES, fill=BOTH) 

#功能按钮 
wzwF = frame(root, TOP)
start_btn = Button(wzwF, text="启动", command=start_server)
start_btn.pack(side=LEFT, expand=YES, fill=BOTH)
stop_btn = Button(wzwF, text="停止", command=stop_server)
stop_btn.pack(side=LEFT, expand=YES, fill=BOTH)
clear_btn = Button(wzwF, text="清除", command=clear)
clear_btn.pack(side=LEFT, expand=YES, fill=BOTH)
about_btn = Button(wzwF, text="关于", command=show_info)
about_btn.pack(side=LEFT, expand=YES, fill=BOTH)
quit_btn = Button(wzwF, text="退出", command=quit)
quit_btn.pack(side=LEFT, expand=YES, fill=BOTH)

#文本显示框
clearF = frame(root, BOTTOM)
scrollbar = Scrollbar(clearF, orient=VERTICAL)
listbox = Listbox(clearF, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)

#启动服务器
start_server()
            
root.mainloop()