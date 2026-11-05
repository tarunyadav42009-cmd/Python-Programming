from tkinter import *
from tkinter.ttk import *
k=Tk()
k.title("Welcome to app")
k.geometry('350x200')
rad1=Radiobutton(k,text='first',value=1)
tad2=Radiobutton(k,text='second',value=2)
rad3=Radiobutton(k,text='third',value=3)
rad1.grid(column=0,row=0)
tad2.grid(column=0,row=1)
rad3.grid(column=0,row=2)
k.mainloop()
