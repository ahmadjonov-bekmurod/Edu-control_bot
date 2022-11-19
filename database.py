import sqlite3

mydb = sqlite3.connect("./db.sqlite", check_same_thread=False)
mycursor = mydb.cursor()
