#coding=utf-8
from Tkinter import *

import os
import config
import string
  
def Button1():
    
    a = 1024
    b = 6355
    i = 0
    i = text.getvar()
#    print tmp
#    i=0
#    try:
#        i = string.atoi(tmp)
#    except ValueError:
#        print '非法字符'
    print i
    if   i <= a or i >=b :
        listbox.insert(END, "I's wrong!")
        text.delete(0,END)
    
    else:
        listbox.insert(END, i)
        text.delete(0,END)
        print 'ssss'
#         config.PORT = i
         
    listbox.insert(END, 'Down')
    text.delete(0,END)     

    
def Button2():

    listbox.delete(0,END)

def Button3():
   
    listbox.insert(END, 'Thanks!') 
    
root = Tk()   
root.title("login")





label1 = Label(root, text="Please choice a nembuer from ")
label2 = Label(root, text="1024 to 6355 ")

label3 = Label(root, text="PORT:")  
text = Entry(root)

button1 = Button(root, text="login", command=Button1)

button2 = Button(root, text="clear", command=Button2)

button3 = Button(root, text="quit", command=Button3)

scrollbar = Scrollbar(root, orient=VERTICAL)

listbox = Listbox(root, yscrollcommand=scrollbar.set)

scrollbar.configure(command=listbox.yview)



label1.pack()
label2.pack()
label3.pack(side=LEFT, fill=X, expand=1)
text.pack(side=LEFT)

button1.pack(side=LEFT,padx=10,pady=10)


button2.pack()
button3.pack(side=BOTTOM)



listbox.pack(side=LEFT,fill=BOTH, expand=1)

scrollbar.pack(side=RIGHT, fill=Y)



root.mainloop() 





