'''
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE registration(id INT,empname VARCHAR(20),mobile BIGINT,Salary BIGINT)")

print("Table is created ")
'''

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")

mycursor=mydb.cursor()

sql="INSERT INTO registration(id,empname,mobile,salary)VALUES(%s,%s,%s,%s)"
val=[
    ("2","JEET","923466212","60000"),
    ("3","GEET","843426792","50000")       
]
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")


