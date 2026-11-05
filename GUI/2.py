from tkinter import *

from tkinter import scrolledtext
window = Tk()
window.title("Welcome to GUI programming!")
lbl=Label(window,text="Hello")
lbl2=Label(window,text="Print",font=("Arial Bold",50))
btn=Button(window,text="click me",bg="orange",fg="red")
add=scrolledtext.ScrolledText(window,width=20,height=2)
txt=Text(window,width=20,height=2)
lbl.grid(column=1,row=0)
lbl2.grid(column=1,row=1)
btn.grid(column=0,row=2)
add.grid(column=0,row=3)
txt.grid(column=0,row=4)
window.geometry('350x200')
window.mainloop()
