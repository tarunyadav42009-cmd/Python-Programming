'''
from tkinter.ttk import *
from tkinter import *
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")

mycursor=mydb.cursor()



k=Tk()
k.geometry('350x250')
l1=Label(k,width=9,height=2,text="Name")
name = Text(k, width=10, height=1)
l2=Label(k,width=12,height=2,text="Phone Number")
no= Text(k, width=10, height=1)
l1.grid(row=0,column=0)
name.grid(row=0,column=1)
l2.grid(row=1,column=0)
no.grid(row=1,column=1)

k.mainloop()
'''


from tkinter.ttk import *
from tkinter import *
import mysql.connector

# 1. Establish the database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor = mydb.cursor()

# 2. Function to fetch text from UI and insert into MySQL
def insert_data():
    # Get text from the Text widgets (1.0 means line 1, character 0 to END)
    user_name = name.get("1.0", "end-1c").strip()
    user_phone = no.get("1.0", "end-1c").strip()
    
    # Validation to ensure fields aren't empty
    if user_name and user_phone:
        try:
            # SQL Query (Replace 'your_table_name' with your actual table name)
            sql = "INSERT INTO get(name, Mobile_Number) VALUES (%s, %s)"
            val = (user_name, user_phone)
            
            mycursor.execute(sql, val)
            mydb.commit() # Important: Saves the changes to the database
            
            print("Data inserted successfully!")
            
            # Clear the text boxes after successful insertion
            name.delete("1.0", END)
            no.delete("1.0", END)
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Please fill in both fields.")

# 3. UI Setup
k = Tk()
k.geometry('350x250')

l1 = Label(k, width=9, height=2, text="Name")
name = Text(k, width=10, height=1)

l2 = Label(k, width=12, height=2, text="Phone Number")
no = Text(k, width=10, height=1)

# 4. Add a Submit Button linked to the function
btn = Button(k, text="Submit", command=insert_data)

# Grid Layout
l1.grid(row=0, column=0)
name.grid(row=0, column=1)
l2.grid(row=1, column=0)
no.grid(row=1, column=1)
btn.grid(row=2, column=0, columnspan=2, pady=10) # Centered below fields

k.mainloop()
