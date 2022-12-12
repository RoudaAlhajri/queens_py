#!/usr/bin/python

import sqlite3
def create_table():
  conn = sqlite3.connect('queens.db') 
  print("Opened database successfully")
  conn.execute('''CREATE TABLE users(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,NAME TEXT NOT NULL,username TEXT NOT NULL,password TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50));''')
  print("Table created successfully")
  conn.close()




create_table()
