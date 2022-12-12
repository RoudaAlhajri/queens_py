#!/usr/bin/python
from hashlib import sha256
import sqlite3
#this function to hash the password 
#before using it or comparing it to the database record
def generate_hash(value):
  return(sha256(value.encode('utf-8')).hexdigest())

# to create a new user
def add_user(NAME,username, password, AGE,ADDRESS):
  
  password=generate_hash(password)
  conn.execute("INSERT INTO users (NAME,username, password, AGE,ADDRESS) VALUES ( '"+str(NAME)+"', '"+str(username)+"', '"+str(password)+"', '"+str(AGE)+"', '"+str(ADDRESS)+"')")



  conn.commit()
  print("user added successfully")
  

def login():

  username_ = input('username: ')
  password_ = input('password: ')
  password=generate_hash(password_)
  sqlstr="SELECT id, name, address from users where username='"+str(username_)+"' and password='"+str(password)+"'"
  cursor = conn.execute(sqlstr)
  for row in cursor:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])


conn = sqlite3.connect('queens.db')
print("Opened database successfully")
#name_ = input('Name: ')
#username_ = input('username: ')
#password_ = input('password: ')
#age_ = input('age: ')
#address_ = input('address: ')
#add_user(name_,username_, password_, age_,address_)
login()

conn.close()
