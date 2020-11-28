import sqlite3,os
import numpy as np 
import pandas as pd 


if(os.path.exists("./users.db")):
	os.remove("./users.db")
else:
	pass



class registration:
	def __init__(self,cur):
		self.cur = cur

	def add_user(self, name):
		self.cur.execute("SELECT * FROM users WHERE username=(?);", (name,))
		check = self.cur.fetchone()
		if check is not None:
			print("Username {} already exists !!!".format(name))
		else:
			self.cur.execute("INSERT INTO users (username) VALUES (?);", (name,))
			print("{} is added.".format(name))


	def rm_user(self, name):
		self.cur.execute("SELECT * FROM users WHERE username=(?);", (name,))
		check = self.cur.fetchone()
		if check is not None:
			cur.execute("DELETE FROM users WHERE username=(?);", (name,))
			print("{} is deleted".format(name))
		else:
			print("{} is not found in database".format(name))


	def print_db(self):
		for row in self.cur.execute("SELECT * FROM users").fetchall():
			print(row)

con = sqlite3.connect("users.db")
cur = con.cursor()
cur.execute("create table users(username text(255))")

reg = registration(cur)
#user = input("Enter your Name : ")
user = "Anonymous"
reg.add_user(user)


reg.print_db()
