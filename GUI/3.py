import tkinter as tk

def show_text():
    # .get() retrieves the text typed into the field
    user_input = text_field.get()
    print(f"User typed: {user_input}")

# Create the main window
root = tk.Tk()
root.title("Text Field Example")
root.geometry("300x150")

# Create the text field (Entry widget)
text_field = tk.Entry(root, width=30)
text_field.pack(pady=20)

# Create a button to submit the text
submit_btn = tk.Button(root, text="Submit", command=show_text)
submit_btn.pack()

root.mainloop()
