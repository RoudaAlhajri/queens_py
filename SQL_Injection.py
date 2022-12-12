#!/usr/bin/python
#this code to show sql injection example by using 
# id: 5 OR 1=1. as input 
import sqlite3

conn = sqlite3.connect('queens.db')
print("Opened database successfully")
uid = input('id: ')
id=uid.replace(" ", "")
sqlstr=f"SELECT id, name, address from users where id={id}"
print(id)
cursor = conn.execute(sqlstr)
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   


conn.close()






