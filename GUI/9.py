from tkinter import *
from tkinter.ttk import *

k = Tk()
k.title("Welcome to universe!")
k.geometry('540x270')

# Label welcoming the user
uni = Label(
    k,
    text="Welcome to dumy universe of pixels of only white color and select your character",
    padding=20,
)

a = StringVar()
rad1 = Radiobutton(k, text='Male', value="male", variable=a)
tad2 = Radiobutton(k, text='Female', value="female", variable=a)


def dragon():
    print("you have selected", a.get())


btn = Button(k, text="Click me", command=dragon)

# --- Layout arrangement using Grid ---
# Let the main label span across 2 columns
uni.grid(column=0, row=0, columnspan=2, pady=20)

# Position radio buttons side-by-side in rows directly under the label
rad1.grid(column=0, row=1, padx=10, pady=10)
tad2.grid(column=1, row=1, padx=10, pady=10)

# Center the button underneath both options by spanning 2 columns
btn.grid(column=0, row=2, columnspan=2, pady=10)

k.mainloop()
