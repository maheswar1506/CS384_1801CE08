import sqlite3
import os
import sys
import keyboard
import time
import hashlib
import numpy as np 
import pandas as pd 
import keyboard as kb
import multiprocessing as mp
import tkinter as tk
from tkinter import messagebox



if(os.path.exists("./users.db")):
    os.remove("./users.db")
else:
    pass


def hashing(password):
    return hashlib.sha512(password.encode()).hexdigest()

def add_user(username, roll, password, whatsapp):
    cur.execute("SELECT * FROM users WHERE username=(?);", (username,))
    check = cur.fetchone()
    if username == "" or roll == "" or password == "" or whatsapp =="":
        tk.messagebox.showerror("Error", "All the fields are required")
    elif check is not None:
        tk.messagebox.showerror("Error", "Username {} already exists !!!".format(username))
    else:
        cur.execute("INSERT INTO users (username, roll, password, whatsapp) VALUES (?,?,?,?);", (username, roll, hashing(password), whatsapp))
        #tk.messagebox.showinfo("{} Succesfully Registered !!!".format(username))

def login_check(roll, password):
    cur.execute("SELECT username,password FROM users WHERE roll=(?);", (roll,))
    check = cur.fetchone()
    if check is not None:
        if password == check[1]:
            tk.messagebox.showerror("welcome {}".format(check[0]))
            program_dict["username"] = check[0]
        else:
            tk.messagebox.showerror("Incorrect Password !!!")
    else:
        print("{} is not found in database".format(username))

LARGE_FONT= ("Verdana", 12)


class main(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #****** DataBase *******
        # Table 1
        global con
        global cur
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            roll TEXT NOT NULL,
            password TEXT NOT NULL,
            whatsapp INTEGER NOT NULL)""")

        # Table 2
        sql_query_for_table_2 = "CREATE TABLE marks (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,roll TEXT NOT NULL,"
        files = os.listdir("./quiz_wise_questions")
        files = [file.split(".")[0]+" REAL" for file in files]
        sql_query_for_table_2 = sql_query_for_table_2 + ",".join(files) + ",total REAL)"
        cur.execute(sql_query_for_table_2)

        details = [("Maheswar Reddy", "1801CE08", "pass123", 8790708058),
                    ("Rohit Bheema", "1801EE24", "hello123", 8553428938),
                    ("Santosh Kumar Reddy", "1801CS32", "Password", 9848752725)]

        for user_detail in details:
            add_user(*user_detail)


        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (start_page, login_page, reg_page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start_page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


        
class start_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        main_frame = tk.Frame(self, bg="orange red")
        main_frame.place(relx=0.5, rely=0.5, width=850, height=550, anchor="center")

        login_btn = tk.Button(self, text="Login",bg="RoyalBlue2", bd=0, cursor="hand2", command=lambda: controller.show_frame(login_page)).place(relx=0.4, rely=0.4, width=100, height=50)      
        reg_btn = tk.Button(self, text="Register",bg="RoyalBlue2", bd=0, cursor="hand2", command=lambda: controller.show_frame(reg_page)).place(relx=0.4, rely=0.5, width=100, height=50)




class login_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, width=850, height=550, bg="skyblue")
        tk.Label(self, text="Login", bg="deepskyblue", font=50, fg="red4").place(relx=0, rely=0, relwidth=1, height=50)
        tk.Label(self, text="Username", font=50, bg="skyblue", fg="red4",anchor="w").place(relx=0.05, rely=0.25, relwidth=1, height=25)
        self.text_user = tk.Entry(self, font=("times new roman", 15))
        self.text_user.place(relx=0.05, rely=0.35, width=250, height=30)
        tk.Label(self, text="Password", font=50, bg="skyblue", fg="red4",anchor="w").place(relx=0.05, rely=0.45, relwidth=1, height=25)
        self.text_paswd = tk.Entry(self, font=("times new roman", 15))
        self.text_paswd.place(relx=0.05, rely=0.55, width=250, height=30)
        log_in = tk.Button(self, text="Login", bg="dark green", fg="white", command=lambda: controller.show_frame(start_page)).place(relx=0.05, rely=0.7, width=100, height=25)



class reg_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=850, height=550, bg="thistle3")
        tk.Label(self, text="Registration", bg="steel blue", font=50, fg="red4").place(relx=0, rely=0, relwidth=1, height=50)
        tk.Label(self, text="Name", font=50, fg="red4", bg="thistle3", anchor="w").place(relx=0.05, rely=0.15, relwidth=1, height=25)
        self.text_name = tk.Entry(self, font=("times new roman", 15))
        self.text_name.place(relx=0.05, rely=0.2, width=250, height=30)
        tk.Label(self, text="Roll", font=50, fg="red4", bg="thistle3", anchor="w").place(relx=0.05, rely=0.25, relwidth=1, height=25)
        self.text_roll = tk.Entry(self, font=("times new roman", 15))
        self.text_roll.place(relx=0.05, rely=0.3, width=250, height=30)
        tk.Label(self, text="Password", font=50, fg="red4", bg="thistle3", anchor="w").place(relx=0.05, rely=0.35, relwidth=1, height=25)
        self.text_passwd = tk.Entry(self, font=("times new roman", 15))
        self.text_passwd.place(relx=0.05, rely=0.4, width=250, height=30)
        tk.Label(self, text="Whatsapp Number", font=50, fg="red4", bg="thistle3", anchor="w").place(relx=0.05, rely=0.45, relwidth=1, height=25)
        self.text_number = tk.Entry(self, font=("times new roman", 15))
        self.text_number.place(relx=0.05, rely=0.5, width=250, height=30)
        reg_btn = tk.Button(self, text="Register", bg="dark green", fg="white", command=lambda: self.call_fun(controller, self.text_name.get(), self.text_roll.get(), self.text_passwd.get(), self.text_number.get())).place(relx=0.05, rely=0.6, width=100, height=25)

    def call_fun(self, controller, username, roll, password, whatsapp):
        add_user(username, roll, password, whatsapp)
        controller.show_frame(login_page)



app = main()
app.mainloop()