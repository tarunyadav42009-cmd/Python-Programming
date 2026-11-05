from tkinter import *
from tkinter.ttk import *
k=Tk()
k.title("Welcome to app")
k.geometry('350x200')
a=StringVar()
rad1=Radiobutton(k,text='first',value="male",variable=a)
tad2=Radiobutton(k,text='second',value="female",variable=a)
def dragon():
    print("you have selected",a.get())
btn=Button(k,text="Click me",command=dragon)
rad1.grid(column=0,row=0)
tad2.grid(column=1,row=0)
btn.grid(column=2,row=0)
k.mainloop()
