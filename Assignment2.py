# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:40:53 2022

@author: Najmun Nahar
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
        lbl_title = ttk.Label(frame, text="ICET Student Survey",background='light green',font=('Arial','16','bold','italic'),padding=10).grid(column=1,row=0,sticky=(W, E)) 
        
        #row 1
        lbl_full_name = ttk.Label(frame,text='Full name:',background='light green',font=myfont,padding=10).grid(column=0,row=1,sticky=(W, E))      
        #taking inputs                        
        self.username = StringVar()
        self.username.set('Najmun Nahar')
        name = ttk.Entry(frame,textvariable=self.username).grid(column=1,row=1,sticky=(W,E)) 
        
        #row 2        
        ttk.Label(frame, text='Residency:',background='light green',font=myfont,padding=10).grid( column=0, row=2, sticky=(W, E))
        panel = ttk.Frame(frame,style='My.TFrame') 
        panel.grid(column=1, row=2, sticky=(W, E))
        self.residency = StringVar(value='dom')
        ttk.Radiobutton(panel, text='Domestic', variable=self.residency, value='dom',style='Wild.TRadiobutton').grid(column=0, row=0, sticky=(W)) 
        ttk.Radiobutton(panel, text='International', variable=self.residency,value='intl',style='Wild.TRadiobutton').grid(column=0, row=1, sticky=(W))
        
        #row 3
        ttk.Label(frame, text='Program:',background='light green',font=myfont,padding=10).grid(column=0, row=3, sticky=(W, E))
        self.program = StringVar()
        combo = ttk.Combobox(frame, textvariable=self.program)
        combo['values']= ("AI", "Gaming", "Health", "Software")
        combo.current(2)
        combo.grid(row = 3, column = 1,sticky=(W))
        
        #row 4      
        ttk.Label(frame, text='Courses:',background='light green',font=myfont,padding=10).grid( column=0, row=4, sticky=(W, E))
        panel = ttk.Frame(frame,style='My.TFrame',padding=(0,0,0,10))
        panel.grid(column=1, row=4, columnspan=4, sticky=(W, E))        
        self.comp100 = StringVar(value='comp100')
        self.comp213 = StringVar()
        self.comp120 = StringVar()        
        ttk.Checkbutton( panel,text='Programming I',variable=self.comp100,offvalue='',onvalue='comp100',style='Green.TCheckbutton').grid(column=0, row=0, sticky=(W))
        ttk.Checkbutton( panel, text='Web Page Design',variable=self.comp213, onvalue='comp213',offvalue='',style='Green.TCheckbutton').grid(column=0, row=1, sticky=(W))
        ttk.Checkbutton( panel, text='Software Engineering Fundamentals',variable=self.comp120, onvalue='comp129',offvalue='',style='Green.TCheckbutton').grid(column=0, row=2, sticky=(W))
        
        #functions
        def read_form(*args):
            messagebox.showinfo(title='Information', message=f'Username: {self.username.get()} \nResidency: {self.residency.get()}\nCourses:{self.comp100.get()} {self.comp120.get()} {self.comp213.get()}\nProgram: {self.program.get()}')
            
        def resetValues(*args):
            self.username.set('Najmun Nahar')
            self.residency.set('dom')
            self.program.set('Health')
            self.comp100.set('comp100')
            self.comp213.set('')
            self.comp120.set('') 
            
        def closeWindow(*args):
            root.destroy()
            
        #row 5
        button = ttk.Button(frame, text='Reset',command=resetValues,padding=5).grid(column=0, row=5, sticky=NSEW)
        ttk.Button(frame, text='Ok',padding=5,command=read_form).grid(column=1, row=5, sticky=NSEW)
        ttk.Button(frame, text='Exit',padding=5,command=closeWindow).grid(column=2, row=5, sticky=NSEW)
        
        
        # start GUI
        root.mainloop()
 
#call class
icetSurvey()
        
        