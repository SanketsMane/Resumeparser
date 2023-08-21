import tkinter as tk
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
window.geometry('400x400')
window.title('Resume Parser')
img=Image.open('images/e1.jpg')

bg=ImageTk.PhotoImage(img)
label=tk.Label(window,image=bg)
label.place(x=0,y=0)

window.configure(background='sky blue')
clicked=tk.StringVar()
count=0
def search_into_files(search_key1):
    key1=(search_key1.get())
    path='NewResume'
    files=os.listdir(path)
    for i in files:
        with open(r"NewResume/"+i,"r") as file3:
            content=file3.read()
            if(key1 in content):
                #print(content.index(key1))
                print("exist in",i)
            else:
                print("not exist in",i)


    
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

        
    return

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
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    numOfPages=pdfreader.numPages
    file_name=os.path.basename(obj_file)
    file_name1,file_extension1=os.path.splitext(file_name)

    file2=open(r"NewResume/"+file_name1+".txt","a")
    for i in range(numOfPages):
        page=pdfreader.getPage(i)
        text=page.extractText()
        file2.write(text)
        """x=pdfreader.numPages
    pageobj=pdfreader.getPage(0)"""
    #file_name1,file_extension1=os.path.splitext(obj_file)
        
    

    #text=pageobj.extractText()
    
    

    #print(obj_file)
    return

def choose():
    global count
    count=count+1
    filetypes=(('text files','*.txt'),('docx files','*.docx'),('pdf files','*.pdf'))
    file=filedialog.askopenfilename( title='open files', initialdir='/',filetypes=filetypes)
    showinfo(title='selected file',message=file)
    """dest_dir=r'Resume'
    for fname in file:
        shutil.copy2(os.path.join(file,fname),dest_dir)
    """
    
    messsage1=file
    E1=tk.Listbox(window,height=5,width=30)
    if count==1:
        E1.insert(1,messsage1)
    if count==2:
        E1.insert(2,messsage1)
    E1.grid(row=1,column=0)
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

label=tk.Label(text="Resume Parser",foreground="white",background="black",width=60)
label.grid(row=0,column=0)

button1=tk.Button(window,text="Upload",command=choose)
button1.grid(row=1 ,column=1)
i=i+1
key3=tk.StringVar()
e2=tk.Entry(window,textvariable=key3,bd=5)
e2.grid(row=2,column=0)
search_key=e2.get()
search_into_files= partial(search_into_files,key3)
button2=tk.Button(window,text="Search",command=search_into_files)
button2.grid(row=2,column=1)
"""button=tk.Button(window,text="convert",command=convert)
button.grid(row=2,cloumn=0)"""
window.mainloop()
