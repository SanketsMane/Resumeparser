import tkinter as tk
from tkinter import *
import os
import shutil
from tkinter.messagebox import showinfo
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from pathlib import Path
import PyPDF2
import docx2txt
from functools import partial
from PIL import ImageTk,Image
from tkinter import ttk
#import askopenfile
i=0
window=tk.Tk()
window.geometry("1199x600+100+50")
window.resizable(False,False)
window.title('Resume Parser')
bg=ImageTk.PhotoImage(file='images/e1.jpg')
bg_image=tk.Label(window,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
#img=Image.open('images/e1.jpg')


#class Abc:
#    def __init__(self,window):

#label2=Label(Frame_neww,text="This is label")
#label2.place(x=10,y=20)
#bg=ImageTk.PhotoImage(img)
#label=tk.Label(window,image=bg)
#label.place(x=0,y=0)

#window.configure(background='sky blue')
clicked=tk.StringVar()
#count=0\
"""def clear1():
    Frame_neww.destroy()"""
def logout1():
    window.destroy()
    os.system('python login.py')
    return
def open_files1(i2):
    path1='E:\\All files\\final\\Resume\\'
    os.startfile(path1+i2)
    
    return

def search_into_files(search_key1):
    def clear1():
        Frame_neww.destroy()
        return
    
                                

    i4=0
    Frame_neww=Frame(window)
    Frame_neww.place(x=300,y=450,width=550,height=140)

    
    #global label5
    #global button5
    
    key1=(search_key1.get())
    if key1=="":
        tk.messagebox.showerror("Error","Enter the search key")
    else:
        
        
        
        path='NewResume'
        files=os.listdir(path)
        path1='Resume'
        files1=os.listdir(path1)
        for i in files:
            with open(r"NewResume/"+i,"r") as file3:
                content=file3.read()
                if (key1 in content) or (key1.lower() in content) or (key1.upper() in content) or (key1.title() in content):
                    #print(content.index(key1))
                    #print("exist in",i)
                    
                
                    #with open(r"Resume/"+i1,"r")
                    file_name1,file_extension1=os.path.splitext(i)
                    for i1 in files1:
                        with open(r"Resume/"+i1,"r") as file4:
                            file_name2,file_extension2=os.path.splitext(i1)
                            if(file_name1==file_name2):
                                
                                y1=20+i4
                                #global label5
                                label5=tk.Label(Frame_neww,text=i1)
                                label5.place(x=50,y=y1)
                                y2=20+i4
                                #global button5
                                button5=tk.Button(Frame_neww,text="Open" ,command=partial(open_files1,i1))
                                button5.place(x=400,y=y2,width=100,height=20)
                                

                                button6=Button(window,text="Clear",command=clear1)
                                button6.place(x=680,y=410, width=100,height=20)
                                                        

                                #label5.destroy()
                                #button5.destroy()
                                #print(y1)
                                #print(y2)
                                #print(i4)
                                i4=i4+20
                                #print(i4)
                                #print(i1)
                                
                            
               
        """else:
            print("not exist in",i)
            #Frame1.destroy()"""
    return



    
    """for filename in os.listdir("NewResume"):
        with open(os.path.join("NewResume",filename),'r') as f:
            content=f.read()
            if key1 in content:
                #print(content.index(key1))
                print("exist in",f)
                print(key1)
            else:
                print("not exist in",f)

            
    """        
        #entries=os.listdir("NewResume/")
    """path='NewResume'
    files=os.listdir(path)
    for i in files:
        with open(r"NewResume/"+i,"r") as file3:
            lines=file3.readlines()
            for row in lines:
                if row.find(key1)!=-1:
                    print("exist in",i)
                else:
                    print("not exist in",i)
                    """
                    
    """content=file3.read()
            if(key1 in content):
                #print(content.index(key1))
                print("exist in",i)
            else:
                print("not exist in",i)
                """

        
    

def text_to_text1(file1):
    shutil.copy(file1,'NewResume')
def docx_to_text1(file1):
    obj_file=file1
    my_txt=docx2txt.process(obj_file)
    
    file_name=os.path.basename(obj_file)
    file_name1,file_extension1=os.path.splitext(file_name)
    file2=open(r"NewResume/"+file_name1+".txt","a")
    file2.writelines(my_txt)

    return

def pdf_to_text1(file1):
    obj_file=file1
    pdffileobj=open(obj_file,'rb')
    pdfreader=PyPDF2.PdfReader(pdffileobj)
    numOfPages=len(pdfreader.pages)
    file_name=os.path.basename(obj_file)
    file_name1,file_extension1=os.path.splitext(file_name)

    file2=open(r"NewResume/"+file_name1+".txt","a")
    for i in range(numOfPages):
        page=pdfreader.pages[i]
        text=page.extract_text()
        file2.write(text)
        """x=pdfreader.numPages
    pageobj=pdfreader.getPage(0)"""
    #file_name1,file_extension1=os.path.splitext(obj_file)
        
    

    #text=pageobj.extractText()
    
    

    #print(obj_file)
    return

def choose(E1):
    #global count
    #count=count+1
    filetypes=(('text files','*.txt'),('docx files','*.docx'),('pdf files','*.pdf'))
    file=filedialog.askopenfilename( title='open files', initialdir='/',filetypes=filetypes)
    showinfo(title='selected file',message=file)
    """dest_dir=r'Resume'
    for fname in file:
        shutil.copy2(os.path.join(file,fname),dest_dir)
    """
    
    messsage1=file
    
    
    #E1=tk.Entry(window,height=5,width=30,fg="black").place(x=350,y=300)
    #E1=tk.Listbox(window,height=5,width=30,bd=8,bg="#6162FF",fg="white").place(x=500,y=450,width=180,height=40)
    E1.insert(1,messsage1)
    """"if count==1:
        E1.insert(1,messsage1)
    if count==2:
        E1.insert(2,messsage1)"""
    #E1.grid(row=1,column=0)
    newpath=shutil.copy(file,'Resume')
    file_name,file_extension=os.path.splitext(messsage1)
    if(file_extension=='.pdf'):
        pdf_to_text1(file)
    if(file_extension=='.docx'):
        docx_to_text1(file)
    if(file_extension=='.txt'):
        text_to_text1(file)
    #i=i+1
    #file.close()
    
    """if file:
        fob=open(file,'r')
        #if file.extension!= 
        #print(fob.read())
    else:
        print("No file chosen")
"""

"""options=[
    "doc",
    "pdf",
    "text"]
drop=tk.OptionMenu(window,clicked,*options)
drop.pack()"""

label=tk.Label(text="Resume Parser",font=("impact",35,"bold"),fg="#6162FF",bg="white").place(x=450,y=200)
#label.grid(row=0,column=0)
button5=tk.Button(window,text="Logout",command=logout1,bd=8,font=("Goudy old style",15,),bg="#6162FF",fg="white").place(x=780,y=110,width=80,height=40)
label=tk.Label(text="FILES",font=("impact",20,"bold"),fg="#6162FF",bg="white").place(x=530,y=410,width=100,height=20)

key4=tk.StringVar()
E1=tk.Entry(window,textvariable=key4,bd=5,font=("Goudy old style",15,"bold"),bg="#E7E6E6")
E1.place(x=350,y=300,width=320,height=35)

button1=tk.Button(window,text="Upload",command=partial(choose,E1),bd=8,font=("Goudy old style",15,),bg="#6162FF",fg="white").place(x=680,y=300,width=180,height=40)
#button1.grid(row=1 ,column=1)
i=i+1
key3=tk.StringVar()
e2=tk.Entry(window,textvariable=key3,bd=5,font=("Goudy old style",15,"bold"),bg="#E7E6E6")
e2.place(x=350,y=350,width=320,height=35)
#e2.grid(row=2,column=0)
search_key=e2.get()
search_into_files= partial(search_into_files,key3)
button2=tk.Button(window,text="Search",command=search_into_files,bd=8,font=("Goudy old style",15,),bg="#6162FF",fg="white").place(x=680,y=350,width=180,height=40)

#search_into_files.label5.destroy()
#search_into_files.button5.destroy()

#button2.grid(row=2,column=1)
"""button=tk.Button(window,text="convert",command=convert)
button.grid(row=2,cloumn=0)"""
window.mainloop()
