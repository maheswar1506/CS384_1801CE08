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

#        for user_detail in details:
#            add_user(*user_detail)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (start_page, login_page, reg_page, display_quiz ,display_ques):

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
        log_in = tk.Button(self, text="Login", bg="dark green", fg="white", command=lambda: self.login_check(controller, self.text_user.get(), hashing(self.text_paswd.get()))).place(relx=0.05, rely=0.7, width=100, height=25)

    def login_check(self, controller, roll, password):
        cur.execute("SELECT username,password FROM users WHERE roll=(?);", (roll,))
        check = cur.fetchone()
        if check is not None:
            if password == check[1]:
                tk.messagebox.showinfo("welcome {}".format(check[0]))
                program_dict["username"] = check[0]
                controller.show_frame(display_quiz)
            else:
                tk.messagebox.showerror("Error", "Incorrect Password !!!")
        else:
            tl.messagebox.showerror("Error", "{} is not found in database".format(username))

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
        reg_btn = tk.Button(self, text="Register", bg="dark green", fg="white", command=lambda: self.add_user(controller, self.text_name.get(), self.text_roll.get(), self.text_passwd.get(), self.text_number.get())).place(relx=0.05, rely=0.6, width=100, height=25)

    def add_user(self, controller, username, roll, password, whatsapp):
        cur.execute("SELECT * FROM users WHERE username=(?);", (username,))
        check = cur.fetchone()
        if username == "" or roll == "" or password == "" or whatsapp =="":
            tk.messagebox.showerror("Error", "All the fields are required")
        elif check is not None:
            tk.messagebox.showerror("Error", "Username {} already exists !!!".format(username))
        else:
            cur.execute("INSERT INTO users (username, roll, password, whatsapp) VALUES (?,?,?,?);", (username, roll, hashing(password), whatsapp))
            tk.messagebox.showinfo("{} Succesfully Registered !!!".format(username))
            controller.show_frame(login_page)


class display_quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=850, height=550, bg="thistle3")
        files = os.listdir("./quiz_wise_questions")
        quiz_list = list()
        tk.Label(self, text="select quiz", bg="steel blue", font=50, fg="red4", anchor="center", height=5).pack(side="top", expand=False, fill="both")
        frame = tk.Frame(self, bg="thistle3")
        frame.pack()
        listNodes = tk.Listbox(frame, width=20, height=15, font=("Helvetica", 12), bg="forest green")
        listNodes.pack(side="left", fill="y")

        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listNodes.yview)
        scrollbar.pack(side="right", fill="y")

        listNodes.config(yscrollcommand=scrollbar.set)
        for file in files:
            quiz_list.append(file.split(".")[0])
        for x in quiz_list:
            listNodes.insert("end", x)

        quiz_btn = tk.Button(self, text="Start Quiz", bg="dark green", fg="white", command=lambda: self.show(listNodes.get(listNodes.curselection()), quiz_list)).pack()
        controller.show_frame(display_ques)

    def show(self, quiz_name, quiz_list):
        row_list = list()
        if quiz_name not in quiz_list:
            tk.messagebox.showerror("Invalid Quiz Name")
        filename = quiz_name + ".csv"
        df = pd.read_csv(os.path.join("./quiz_wise_questions", filename))
        program_dict["rows"] = list()
        for index, row in df.iterrows():
            row_list.append(row)
            ans_dict[row["ques_no"]] = 0
            if row["compulsory"] == "y":
                ans_dict[row["ques_no"]] = row["marks_wrong_ans"]
        program_dict["rows"] = row_list
        program_dict["row_length"] = len(list(df["ques_no"]))
        program_dict["row"] = 0

class display_ques(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=850, height=550, bg="thistle3")


app = main()
manager = mp.Manager()
global program_dict
global ans_dict
global marks_dict
program_dict = manager.dict()
ans_dict = manager.dict()
marks_dict = manager.dict()
app.mainloop()
