import sqlite3
import os
import sys
import keyboard
import time
import hashlib
import numpy as np 
import pandas as pd
import tkinter as tk 
import keyboard as kb
import threading as th 
import multiprocessing as mp
import warnings
warnings.filterwarnings("ignore")


# Database

if(os.path.exists("./project1_quiz_cs384.db")):
    os.remove("./project1_quiz_cs384.db")
else:
    pass

def unattempted_ques():
    global user_choices
    un_li = list()
    un_li = [int(i)+1 for i in range(len(user_choices)) if (user_choices[i])==-1]
    print("\nunattempted_ques : ", *un_li)

def goto():
    global ques_no
    temp = int(input("Enter the question number to go : "))
    ques_no = temp-1

def to_submit():
    global submit, timing
    temp = input("Do you want to do final submit (yes/no) : ")
    temp.lower()
    if temp=="yes":
        submit = True
        timing.terminate()

def export_db():
    conn = sqlite3.connect('./project1_quiz_cs384.db', isolation_level=None,detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM marks", conn)
    db_df.to_csv('./quiz_wise_responses/database.csv', index=False)
    temp = pd.read_csv('./quiz_wise_responses/database.csv')
    q_li = list(temp["quiz_num"].unique())
    basepath = "./quiz_wise_responses"
    for qu in q_li:
        filename = "scores_q"+str(int(qu))+".csv"
        temp_df = temp[temp["quiz_num"] == qu]
        temp_df.to_csv(os.path.join(basepath,filename),mode="a+",index=False)


def db_entry():
    global user_roll, quiz_num, total_score
    temp_con = sqlite3.connect('project1_quiz_cs384.db')
    temp_cur = temp_con.cursor()
    temp_cur.execute("INSERT INTO marks(roll, quiz_num, total_marks) VALUES (?,?,?);", (user_roll, quiz_num, str(total_score)))
    temp_con.commit()

def individual():
    global user_roll, df, quiz_name, total_score, user_choices, row_length, attempted,correct, wrong
    basepath = "./individual_responses"
    filename = quiz_name + "_" + user_roll+".csv"
    temp = df.copy()
    temp = temp[['ques_no','question','option1','option2','option3','option4','correct_option','marks_correct_ans','marks_wrong_ans','compulsory']]
    li= pd.DataFrame({"marked_choice":user_choices})
    l1 = pd.DataFrame({"Total":[correct, wrong,(row_length-attempted),total_score, temp["marks_correct_ans"].sum()]})
    l2 = pd.DataFrame({"Legend":["Correct Choices", "Wrong Choices", "Unattempted","Marks Obtained", "Total Quiz Marks"]})
    temp = pd.concat([temp, li, l1, l2], axis=1)
    temp.to_csv(os.path.join(basepath, filename), mode="a+", index=False)


def add_user(username, roll, password, whatsapp):
    global con 
    global cur
    cur.execute("SELECT * FROM users WHERE username=(?);", (username,))
    check = cur.fetchone()
    print(check)
    if check is not None:
        print("Username {} already exists !!!".format(username))
    else:
        cur.execute("INSERT INTO users (username, roll, password, whatsapp) VALUES (?,?,?,?);", (username, roll, password, whatsapp))
        print("{} is added.".format(username))
    con.commit()



def login_check(roll, password):
    global con 
    global cur
    cur.execute("SELECT username,password FROM users WHERE roll=(?);", (roll,))
    check = cur.fetchone()
    if check is not None:
        if password == check[1]:
            print("welcome {}".format(check[0]))
        else:
            print("Incorrect Password !!!")
    else:
        print("{} is not found in database".format(username))


def display_and_get_ans():
    global tm, root, timing, q_a, quiz_num, quiz_name, df, user_name, user_roll, user_choices
    global row_length, ques_no, unat_ques, total_score, attempted, correct, wrong, submit
    submit = False 
    attempted = 0
    correct = 0
    wrong = 0
    total_score = 0
    user_choices = [-1 for i in range(row_length)]
    user_marks = list()


    while tm>0 and ques_no<row_length:
        row = df.loc[ques_no]
        print("\n")
        print("Roll: {}".format(user_roll))
        print("Username: {}".format(user_name))
        print("Unattempted Questions: press Ctrl + Alt + U")
        print("Goto Question: press Ctrl + Alt + G")
        print("Final Submit: press Ctrl + Alt + F")
        print("Export Database into CSV:: press Ctrl + Alt + E")
        print("Question {}) {}".format(row["ques_no"], row["question"]))
        print("Option 1) {}".format(row["option1"]))
        print("Option 2) {}".format(row["option2"]))
        print("Option 3) {}".format(row["option3"]))
        print("Option 4) {}".format(row["option4"]))
        print("\n")
        print("Credits if Correct Option: {}".format(row["marks_correct_ans"]))
        print("Negative Marking: {}".format(row["marks_wrong_ans"]))
        comp = ""
        if row["compulsory"] == "y":
            comp = "Yes"
        elif row["compulsory"] == "n":
            comp = "No"
        print("Is Compulsory: ".format(comp))
        print("\n")
        print("Enter your choice as per given choices : ")
        choice = input("Enter Choice: 1, 2, 3, 4, S : ")
        choice = choice.lower()
        if submit:
            break
        user_choices[ques_no] = choice
        ques_no = ques_no +1


    try :
        timing.terminate()
    except Exception as e:
        print(e)
    for i in range(row_length):
        row = df.loc[i]
        if user_choices[i] == "s":
            if row["compulsory"] == "y":
                total_score = total_score - row["marks_wrong_ans"]
                wrong = wrong +1
                attempted = attempted +1
            else:
                pass
        elif (int(row["correct_option"])) == int(user_choices[i]):
            total_score = total_score + int(row["marks_correct_ans"])
            attempted = attempted +1
            correct = correct +1
        else:
            attempted = attempted+1
            wrong = wrong+1
    db_entry()
    individual()
    export_db()

def clear():
    if os.name == "nt":
        command = "cls"
    else:
        command = "clear"
    os.system(command)

def timer():
    global tm, time_label, root
    tm = tm*60
    while tm>0:
        time.sleep(1)
        time_label.destroy()
        mins,secs=(tm//60,tm%60)
        var = str(mins)+':'+str(secs)
        time_label = tk.Label(root,text=var, bg="thistle3", fg="red4")
        time_label.place(x=50,y=20, width=50, height=70)
        root.update()
        tm-=1
    root.destroy()



def hashing(password):
    return hashlib.sha512(password.encode()).hexdigest()


def show_quiz():
    global quiz_num, quiz_name, df, user_name, user_roll, user_choices, user_ans, user_marks, row_length, ques_no, unat_ques
    files = os.listdir("./quiz_wise_questions")
    quiz_list = list()
    row_list = list()
    print("select quiz")
    for file in files:
        quiz_list.append(file.split(".")[0])
    print(*quiz_list)
    print("\n")
    quiz_name = input("Enter the quiz name : ")
    if quiz_name not in quiz_list:
        pass
        #sys.exit("Invalid Quiz Name")
    quiz_num = quiz_name[1:]
    filename = quiz_name + ".csv"
    df = pd.read_csv(os.path.join("./quiz_wise_questions", filename))

    row_length = len(list(df["ques_no"]))
    unat_ques = 0
    ques_no = 0

    # time

    global tm
    global root
    global time_label
    tm = df.columns[-1].split("=")[-1]
    tm = int(tm[0:-1])
    root = tk.Tk()
    root.resizable(False, False)
    root["bg"] = "thistle3"
    root.title("Quiz Timer !!!")
    root.geometry("200x150")
    tk.Label(root, text="Timer : ", bg="thistle3", fg="red4").place(x=10, y=20, width=50, height=70)
    time_label = tk.Label(root, text=str(tm), bg="thistle3", fg="red4")
    time_label.place(x=50,y=20, width=50, height=70)
    global timing
    global q_a
    try:
        timing = mp.Process(target=timer)
        q_a =  th.Thread(target=display_and_get_ans)
        timing.start()
        q_a.start()
        timing.join()
        q_a.join()
    except:
        pass
    root.mainloop()


def login():
    user = input("Enter your Name : ")
    password = hashing(input("Enter your Password : "))
    try:
        login_check(user, password)
        global user_name, user_roll
        cur.execute("SELECT username,roll FROM users WHERE roll=(?);", (user,))
        detail = cur.fetchone()
        user_roll = detail[1]
        user_name = detail[0]
        show_quiz()
    except Exception as e:
        print(e)



def register():
    global con 
    global cur
    user = input("Name : ")
    roll = input("Roll : ")
    password = hashing(input("Password : "))
    whatsapp = input("Whatsapp Number : ")
    try:
        add_user(user, roll, password, whatsapp)
    except Exception as e:
        print(e)
        print("Invalid Registration")
    else:
        print("{} completed registration successfuly".format(user))
        login()


kb.add_hotkey("ctrl + alt + u", unattempted_ques)
kb.add_hotkey("ctrl + alt + g", goto)
kb.add_hotkey("ctrl + alt + f", to_submit)
kb.add_hotkey("ctrl + alt + e", export_db)

if __name__ == '__main__':

    # Table 1
    global con 
    global cur
    con = sqlite3.connect("./project1_quiz_cs384.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        roll TEXT NOT NULL,
        password TEXT NOT NULL,
        whatsapp INTEGER NOT NULL)""")
    con.commit()
    # Table 2
    sql_query_for_table_2 = "CREATE TABLE  marks (id INTEGER PRIMARY KEY AUTOINCREMENT,roll TEXT NOT NULL, quiz_num REAL, total_marks REAL)"
    cur.execute(sql_query_for_table_2)

    con.commit()
    clear()

    print("Register")
    print("Login")
    user_inp = input("Enter to Register/Login : ")
    user_inp = user_inp.lower()

    try:
        if user_inp == "login":
            login()
        elif user_inp == "register":
            register()
            pass
            #sys.exit("Please Login to take Quiz !!!")
        else:
            pass
            #sys.exit("Invalid Input !!!")
    except:
        pass
        #sys.exit("Invalid Login !!!")


