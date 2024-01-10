# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:44:12 2022

@author: Moon
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, ttk
from tkinter.font import Font


class icetSurvey:
    
    def __init__(self):
        # create GUI     
        root = Tk()
        root.title("Centennial College")
        root['background']='light green'


        #style for frame
        s=Style()
        s.configure('My.TFrame',background='light green')
        
        #style for radiobuttons
        s2 = ttk.Style() 
        s2.configure('Wild.TRadiobutton', background='light green') 
        
        #style for checkboxes
        s2.configure('Green.TCheckbutton', background='light green') 
        
        #font styles for controls
        myfont = Font(family='Arial', size=10)
        
        #create frame
        frame = ttk.Frame(root,style='My.TFrame')
        frame.pack()
        frame['padding'] = (5,10) 
        
        
        #row 0
        lbl_title = ttk.Label(frame, text="Mid Term",background='light green',font=('Arial','16','bold','italic'),padding=10).grid(column=1,row=0,sticky=(W, E)) 
        
        #row 1
        lbl_full_name = ttk.Label(frame,text='Name:',background='light green',font=myfont,padding=10).grid(column=0,row=1,sticky=(W, E))      
        #taking inputs                        
        self.username = StringVar()
        name = ttk.Entry(frame,textvariable=self.username).grid(column=1,row=1,sticky=(W,E)) 
        
        #row 2
        lbl_Id = ttk.Label(frame,text='ID:',background='light green',font=myfont,padding=10).grid(column=0,row=2,sticky=(W, E))      
        self.stdid = StringVar()
        stdid = ttk.Entry(frame,textvariable=self.stdid).grid(column=1,row=2,sticky=(W,E)) 
        
        #row 3
        lbl_pass = ttk.Label(frame,text='Password:',background='light green',font=myfont,padding=10).grid(column=0,row=3,sticky=(W, E))      
        self.password = StringVar()
        password = ttk.Entry(frame,textvariable=self.password,show='*').grid(column=1,row=3,sticky=(W,E)) 
        
        #row 4        
        ttk.Label(frame, text='Location:',background='light green',font=myfont,padding=10).grid( column=0, row=4, sticky=(W, E))
        panel = ttk.Frame(frame,style='My.TFrame') 
        panel.grid(column=1, row=4, sticky=(W, E))
        self.location = StringVar(value='progress')
        ttk.Radiobutton(panel, text='Progress', variable=self.location, value='progress',style='Wild.TRadiobutton').grid(column=0, row=0, sticky=(W)) 
        ttk.Radiobutton(panel, text='Morning Side', variable=self.location,value='morning side',style='Wild.TRadiobutton').grid(column=0, row=1, sticky=(W))
        
        
       
        #row 5      
        ttk.Label(frame, text='Courses:',background='light green',font=myfont,padding=10).grid( column=0, row=5, sticky=(W, E))
        panel = ttk.Frame(frame,style='My.TFrame',padding=(0,0,0,10))
        panel.grid(column=1, row=6, columnspan=4, sticky=(W, E))        
        self.comp100 = StringVar()
        self.comp213 = StringVar()
        self.comp120 = StringVar()  
        self.comp308 = StringVar()  
        self.comp321 = StringVar()  
        ttk.Checkbutton( panel,text='Programming I',variable=self.comp100,offvalue='',onvalue='comp100',style='Green.TCheckbutton').grid(column=0, row=0, sticky=(W))
        ttk.Checkbutton( panel, text='Web Page Design',variable=self.comp213, onvalue='comp213',offvalue='',style='Green.TCheckbutton').grid(column=0, row=1, sticky=(W))
        ttk.Checkbutton( panel, text='Software Engineering Fundamentals',variable=self.comp120, onvalue='comp129',offvalue='',style='Green.TCheckbutton').grid(column=0, row=2, sticky=(W))
        ttk.Checkbutton( panel, text='Emerging Technologies',variable=self.comp308, onvalue='comp308',offvalue='',style='Green.TCheckbutton').grid(column=0, row=3, sticky=(W))
        ttk.Checkbutton( panel, text='System Integration',variable=self.comp321, onvalue='comp321',offvalue='',style='Green.TCheckbutton').grid(column=0, row=4, sticky=(W))
        

        
        #functions
        def read_form(*args):
            if self.password=='Comp216':
                access='Congrats, you can access the course shell'
            else:
                access='Access denied'
            messagebox.showinfo(title='Information', message=f'Name: {self.username.get()} \nStudent ID: {self.stdid.get()}\nCourses:{self.comp100.get()} {self.comp120.get()} {self.comp213.get()}{self.comp308.get()} {self.comp321.get()}\nLocation: {self.location.get()}\n\n{access}')
            
        def resetValues(*args):
            self.username.set('')
            self.location.set('')
            self.stdid.set('')
            self.password.set('')
            self.comp100.set('')
            self.comp213.set('')
            self.comp120.set('') 
            self.comp308.set('') 
            self.comp321.set('') 
            
            
        def closeWindow(*args):
            root.destroy()
            
        #row 6
        button = ttk.Button(frame, text='Clear',command=resetValues,padding=5).grid(column=0, row=7, sticky=NSEW)
        ttk.Button(frame, text='Ok',padding=5,command=read_form).grid(column=1, row=7, sticky=NSEW)
        ttk.Button(frame, text='Exit',padding=5,command=closeWindow).grid(column=2, row=7, sticky=NSEW)
        
        
        # start GUI
        root.mainloop()
 
#call class
icetSurvey()