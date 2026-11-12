from tkinter import *
from tkinter import scrolledtext, ttk


def submit_details():
    # Grab the values from the inputs
    student_name = name.get()
    student_address = add.get("1.0", END).strip()
    student_course = combo.get()

    # Print the output to the terminal
    print("\n--- Submitted Details ---")
    print(f"Name: {student_name}")
    print(f"Course: {student_course}")
    print(f"Address: {student_address}")
    print("-------------------------")


K = Tk()
K.title("Student Details")
K.geometry("350x260")

# Header
det = Label(K, text="Enter the Details:-", font=("Arial", 10, "bold"))
det.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="w")

# Name Field
lab1 = Label(K, text="Name:", width=10, anchor="w")
lab1.grid(row=1, column=0, padx=10, pady=5)

name = Entry(K, width=23)
name.grid(row=1, column=1, padx=10, pady=5)

# Address Field
add1 = Label(K, text="Address:", width=10, anchor="w")
add1.grid(row=2, column=0, padx=10, pady=5, sticky="n")

add = scrolledtext.ScrolledText(K, width=17, height=3)
add.grid(row=2, column=1, padx=10, pady=5)

# Course Dropdown
course_lbl = Label(K, text="Course:", width=10, anchor="w")
course_lbl.grid(row=3, column=0, padx=10, pady=5)

combo = ttk.Combobox(K, width=20, state="readonly")
combo["values"] = ("BCOM", "BSC", "BTECH", "Diploma", "Undefined")
combo.current(0)
combo.grid(row=3, column=1, padx=10, pady=5)

# Submit Button
submit_btn = Button(
    K, text="Submit", command=submit_details, bg="#4CAF50", fg="white", width=15
)
submit_btn.grid(row=4, column=0, columnspan=2, pady=15)

K.mainloop()
