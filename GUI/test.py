from tkinter import *
from tkinter.ttk import *

k = Tk()
k.title("Welcome to universe!")

# 810x810 -> Digital root of 8+1+0 = 9
k.geometry("810x810")

# width=108 -> 1+0+8 = 9 | height=3 -> We can pad it out with 9 or use 9
uni = Label(
    k,
    text="Welcome to dumy universe of pixels of only white color and select your character",
    width=108,
)
uni.grid(column=9, row=9)  # 9 and 9

# Main container for the buttons to stay side-by-side
# row=18 -> 1+8 = 9 | column=9
options_frame = Frame(k)
options_frame.grid(column=9, row=18)

a = StringVar()
# Putting them side-by-side using roots of 9 inside the frame
rad1 = Radiobutton(options_frame, text="Male", value="male", variable=a)
tad2 = Radiobutton(options_frame, text="Female", value="female", variable=a)

rad1.grid(column=9, row=9, padx=9)  # 9 everywhere
tad2.grid(column=18, row=9, padx=9)  # 18 -> 1+8 = 9


def dragon():
    print("you have selected", a.get())


btn = Button(k, text="Click me", command=dragon)
# row=27 -> 2+7 = 9 | column=9
btn.grid(column=9, row=27, pady=9)

k.mainloop()
