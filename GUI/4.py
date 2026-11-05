
from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to GUI programming!")
window.geometry('3500x200')
combo=Combobox(window)
combo['values']=(1,2,3,4,5,"text")
combo.grid(column=0,row=1)
window.mainloop()