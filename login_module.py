import tkinter as tk
from functools import partial
import os
from PIL import ImageTk,Image
from tkinter import ttk
#import project
from subprocess import Popen
window=tk.Tk()
window.geometry('400x400')
window.title('Login')
img=Image.open('./e1.jpg')

bg=ImageTk.PhotoImage(img)
label=tk.Label(window,image=bg)
label.place(x=0,y=0)
window.configure(background='sky blue')


def login_to_system(user1,pass2):
    user2=(user1.get())
    pass3=(pass2.get())

    if(user2=='admin' and pass3=='admin123'):
        """with open("project.py",'r') as f:
            exec(f.read())"""
        #os.system('python project.py')
        #import project.py
        Popen('python project.py')
    else:
        showinfo(title='Error',message="Invalid Username or Password")
        #print("Invalid Username or Password")
       
    


    return


label10=tk.Label(text="Login Page",foreground="white",background="blue",width=60)
label10.grid(row=0,column=0)

label1=tk.Label(text="Username")
label1.grid(row=3,column=0)

key3=tk.StringVar()
e2=tk.Entry(window,textvariable=key3,bd=5)
e2.grid(row=4,column=0)


label2=tk.Label(text="Password")
label2.grid(row=5,column=0)

key4=tk.StringVar()
e3=tk.Entry(window,textvariable=key4,bd=5,show="*")
e3.grid(row=6,column=0)

user=e2.get()
pass1=e3.get()
login_to_system= partial(login_to_system,key3,key4)

button2=tk.Button(window,text="Login",command=login_to_system)
button2.grid(row=7,column=0)

window.mainloop()
