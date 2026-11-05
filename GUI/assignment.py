

from tkinter import *
##from tkinter import scrolledtext
from tkinter.ttk import *

K=Tk()
'''
det=Label(K,text="Enter the Details:-",width=18,height=1)
det.grid(row=0,column=5)

lab1=Label(K,text="Name",width=9,height=1)
lab1.grid(row=2,column=0)


name=Text(K,width=9,height=1)
name.grid(row=3,column=1)


add1=Label(K,text="Address",width=9,height=1)
add1.grid(column=0,row=4)

add=scrolledtext.ScrolledText(K,width=10,height=1)
add.grid(column=1,row=5)

'''
lab2=Label(K,text="QUALIFICATION",width=9,height=1)
lab2.grid(row=6,column=1)


combo=Combobox(K)

combo['values']=("BCOM","BSC","BTECH","Diploma")
combo.grid(column=2,row=5)
combo.current(1)
K.geometry('350x200')
K.mainloop()



'''

from tkinter import *
from tkinter import scrolledtext
# Removed the wildcard 'from tkinter.ttk import *' to prevent widget conflicts
from tkinter import ttk 

K = Tk()

# Standard Tkinter Labels (using height=1)
det = Label(K, text="Enter the Details:-", width=18, height=1)
lab1 = Label(K, text="Name", width=9, height=1)
name = Text(K, width=9, height=1)
add1 = Label(K, text="Address", width=9, height=1)
add = scrolledtext.ScrolledText(K, width=10, height=1)

# Explicitly using ttk.Combobox and setting values correctly
combo = ttk.Combobox(K)
combo['values'] = ("BCOM", "BSC", "BTECH", "Diploma")

# Layout Configuration
det.grid(row=0, column=0)
lab1.grid(row=2, column=0)
name.grid(row=2, column=1)
add1.grid(column=0, row=3)
add.grid(column=1, row=3)
combo.grid(column=1, row=4)

K.geometry('350x200')
K.mainloop()
'''