#coding=utf-8
#Author: wzw6174
#Create time: 2009-06-04

from Tkinter import *
#from FileDialog import *
import os
import config

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
    MIN_PORT = 1024
    MAX_PORT = 65535
   
    tmp = text.get()
    print tmp
    i = 0
    try:
        i = int(tmp)
    except ValueError:
        listbox.insert(END, "非法字符")
        return 0

    if   i <= MIN_PORT or i >= MAX_PORT :
        listbox.insert(END, "端口范围必须在1024~65535之间!")
    
    else:
        msg = '端口修改成功！现在的端口是', i
        listbox.insert(END, msg)
        listbox.insert(END, '请重启服务器...')
        config.PORT = i
        
    text.delete(0, END)
         
def changePath():

#    fd = LoadFileDialog(root)
#    k = fd.go()
#    text1.delete(0, END)
#    text1.insert(END, k)
#    print k
    tmp = text1.get()
    if cmp(tmp, ''):
        config.apppath = tmp
        listbox.insert(END, '网站根目录修改成功！')
        listbox.insert(END, '请重启服务器...')
       
def Button3():
    pass 
def showInfo():
    listbox.insert(END, '制作小组成员：欧必杰、吴志伟')   
    listbox.insert(END, '鸣谢：115、117') 
    listbox.insert(END, '版本号：1.0 Beta')  
def Button4():

    listbox.delete(0, END)

    

root = Tk()   
root.title("Python-Server")
root.geometry('350x200')

deyF = frame(root, TOP)
label1 = Label(deyF, text="PORT:").pack(side=LEFT, expand=YES, fill=BOTH)

display = StringVar()
text = Entry(deyF, textvariable=display)
text.pack(side=LEFT, expand=YES, fill=BOTH)

button1 = Button(deyF, text="Change", command=changePort)
button1.pack(side=LEFT, expand=YES, fill=BOTH)
   
opsF = frame(root, TOP)
label2 = Label(opsF, text="PATH:") .pack(side=LEFT, expand=YES, fill=BOTH)


text1 = Entry(opsF)
text1.pack(side=LEFT, expand=YES, fill=BOTH)
button2 = Button(opsF, text="Change", command=changePath)
button2 .pack(side=LEFT, expand=YES, fill=BOTH) 
   

#for key in ("01234", "56789"):
#   sumF = frame(root, TOP)
#   for char in key:
#       button(sumF, LEFT, char, lambda w=display, s="%s" % char: w.set\
#              (w.get() + s))
#    
wzwF = frame(root, TOP)
button3 = Button(wzwF, text="quit", command=Button3)
button3.pack(side=LEFT, expand=YES, fill=BOTH)
button4 = Button(wzwF, text="quit", command=Button3)
button4.pack(side=LEFT, expand=YES, fill=BOTH)
button5 = Button(wzwF, text="clear", command=Button4)
button5.pack(side=LEFT, expand=YES, fill=BOTH)
about = Button(wzwF, text="about", command=showInfo)
about.pack(side=LEFT, expand=YES, fill=BOTH)
button6 = Button(wzwF, text="quit", command=root.quit)
button6.pack(side=LEFT, expand=YES, fill=BOTH)
 
clearF = frame(root, BOTTOM)

scrollbar = Scrollbar(clearF, orient=VERTICAL)

listbox = Listbox(clearF, yscrollcommand=scrollbar.set)

scrollbar.configure(command=listbox.yview)

listbox.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()