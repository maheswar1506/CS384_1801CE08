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

# Database

if(os.path.exists("./users.db")):
    os.remove("./users.db")
else:
    pass

def unattempted_ques(program_dict):
    print("unattempted_ques : ")

def goto(program_dict):
    program_dict["row"] = int(input("Enter the Question No : "))

def submit(program_dict):
    print("submit")

def export_db(program_dict):
    pass



"""def ht_kys(program_dict):
    kb.add_hotkey("Ctrl + Alt + U", unattempted_ques, args=(program_dict,))
    kb.add_hotkey("Ctrl + Alt + G", goto, args=(program_dict,))
    kb.add_hotkey("Ctrl + Alt + F", submit, args=(program_dict,))
    kb.add_hotkey("Ctrl + Alt + E", export_db, args=(program_dict,))"""

def row_handling(program_dict,val=False):
    try:
        if val:
            if program_dict["row"] == program_dict["row_length"]-1:
                program_dict["row"] = 0
            else:
                program_dict["row"] = program_dict["row"] + 1

    except:
        pass


def add_user(username, roll, password, whatsapp):
    cur.execute("SELECT * FROM users WHERE username=(?);", (username,))
    check = cur.fetchone()
    if check is not None:
        print("Username {} already exists !!!".format(username))
    else:
        cur.execute("INSERT INTO users (username, roll, password, whatsapp) VALUES (?,?,?,?);", (username, roll, hashing(password), whatsapp))
        print("{} is added.".format(username))


def rm_user(username):
    cur.execute("SELECT * FROM users WHERE username=(?);", (username,))
    check = cur.fetchone()
    if check is not None:
        cur.execute("DELETE FROM users WHERE username=(?);", (username,))
        print("{} is deleted".format(username))
    else:
        print("{} is not found in database".format(username))

def login_check(roll, password):
    cur.execute("SELECT username,password FROM users WHERE roll=(?);", (roll,))
    check = cur.fetchone()
    if check is not None:
        if password == check[1]:
            print("welcome {}".format(check[0]))
            program_dict["username"] = check[0]
        else:
            print("Incorrect Password !!!")
    else:
        print("{} is not found in database".format(username))

def get_details(username):
    cur.execute("SELECT username,roll FROM users WHERE username=(?);", (username,))
    detail = cur.fetchone()
    return [detail[0], detail[1]]

def print_db():
    for row in cur.execute("SELECT * FROM users").fetchall():
        print(row)


def display_and_get_ans(program_dict):
    print("Question {}) {}".format(program_dict["rows"][program_dict["row"]]["ques_no"], program_dict["rows"][program_dict["row"]]["question"]))
    print("Option 1) {}".format(program_dict["rows"][program_dict["row"]]["option1"]))
    print("Option 2) {}".format(program_dict["rows"][program_dict["row"]]["option2"]))
    print("Option 3) {}".format(program_dict["rows"][program_dict["row"]]["option3"]))
    print("Option 4) {}".format(program_dict["rows"][program_dict["row"]]["option4"]))
    print("\n")
    print("Credits if Correct Option: {}".format(program_dict["rows"][program_dict["row"]]["marks_correct_ans"]))
    print("Negative Marking: {}".format(program_dict["rows"][program_dict["row"]]["marks_wrong_ans"]))
    comp = ""
    if program_dict["rows"][program_dict["row"]]["compulsory"] == "y":
        comp = "Yes"
    elif program_dict["rows"][program_dict["row"]]["compulsory"] == "n":
        comp = "No"
    print("Is Compulsory: ".format(comp))
    print("\n")
    choice = input("Enter Choice: 1, 2, 3, 4, S : ")
    if ((comp == "y" and (choice not in [1,2,3,4]))) or (comp == "n" and choice not in [1,2,3,4,""]):
        ans_dict[program_dict["rows"][program_dict["row"]]["ques_no"]] = choice 
        marks_dict[program_dict["rows"][program_dict["row"]]["ques_no"]] = program_dict["rows"][program_dict["row"]]["marks_wrong_ans"]
        print(choice)
        print(-1*program_dict["rows"][program_dict["row"]]["marks_wrong_ans"])
    else:
        ans_dict[program_dict["rows"][program_dict["row"]]["ques_no"]] = choice 
        marks_dict[program_dict["rows"][program_dict["row"]]["ques_no"]] = program_dict["rows"][program_dict["row"]]["marks_correct_ans"]
        print(choice)
        print(program_dict["rows"][program_dict["row"]]["marks_correct_ans"])

    print("\n")
    row_handling(program_dict, True)


def clear():
    if os.name == "nt":
        command = "cls"
    else:
        command = "clear"
    os.system(command)





def hashing(password):
    return hashlib.sha512(password.encode()).hexdigest()


def login():
    #user = input("Enter your Name : ")
    #password = hashing(input("Enter your Password : "))
    #password = hashing(password)
    roll = "1801CE08"
    password = hashing("pass123")
    login_check(roll, password)
    program_dict["roll"] = roll


def register():
    user = input("Name : ")
    roll = input("Roll : ")
    password = input("Password : ")
    password = hashing(password)
    whatsapp = input("Whatsapp Number : ")
    try:
        add_user(user, roll, password, whatsapp)
    except:
        print("Invalid Registration")
    else:
        print("{} completed registration successfuly".format(user))


def show_quiz(program_dict):
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
    filename = quiz_name + ".csv"
    df = pd.read_csv(os.path.join("./quiz_wise_questions", filename))
    program_dict["rows"] = list()
    for index, row in df.iterrows():
        row_list.append(row)
        ans_dict[row["ques_no"]] = ""
        ans_dict[row["ques_no"]] = row["marks_wrong_ans"]
    program_dict["rows"] = row_list
    program_dict["row_length"] = len(list(df["ques_no"]))
    program_dict["row"] = 0


def timer(program_dict):
    count = 1200
    while count:
        mins,secs = divmod(count,60)
        program_dict["timer"] = 'Timer : {:02d}:{:02d}'.format(mins, secs)
        program_dict["counter"] = count
        time.sleep(1)
        count -= 1


def always_display(program_dict, name, roll):
    program_dict["unat_ques"] = 0
    #print("Timer : ", program_dict["timer"])
    print("Roll : ", roll)
    print("Name : ", name)
    print("Unattempted Questions : ", program_dict["unat_ques"])
    print("Goto Question : Press Ctrl + Alt + G")
    print("Final Submit : Press Ctrl + Alt + F")
    print("Export Database into CSV : Press Ctrl + Alt + E")


"""def file_handling(program_dict):
    if program_dict["filename"] in files:
        df = pd.read_csv(os.path.join("./quiz_wise_questions", program_dict["filename"]))
        program_dict["rows"] = list()
        for index, row in df.iterrows():
            program_dict["rows"].append(row)
        program_dict["row_length"] = len(list(df["ques_no"]))
        program_dict["row"] = 0
    else:
        sys.exit("Invalid Quiz !!!")"""

if __name__ == '__main__':

    # Table 1
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

    clear()
    mp.set_start_method("spawn")
    manager = mp.Manager()
    program_dict = manager.dict()
    ans_dict = manager.dict()
    marks_dict = manager.dict()

    kb.add_hotkey("ctrl + alt + u", unattempted_ques, args=(program_dict,))
    kb.add_hotkey("ctrl + alt + g", goto, args=(program_dict,))
    kb.add_hotkey("ctrl + alt + f", submit, args=(program_dict,))
    kb.add_hotkey("ctrl + alt + e", export_db, args=(program_dict,))
    kb.add_hotkey("Enter", row_handling, args=(program_dict, True))

    print("Register")
    print("Login")
    #user_inp = input("Enter to Register/Login : ")
    user_inp = "Login"
    try:
        if user_inp == "Login":
            login()
        elif user_inp == "Register":
            register()
            pass
            #sys.exit("Please Login to take Quiz !!!")
        else:
            pass
            #sys.exit("Invalid Input !!!")
    except:
        pass
        #sys.exit("Invalid Login !!!")

    clear()
    name, roll = get_details(program_dict["username"])
    show_quiz(program_dict)
    clear()
    #timing = mp.Process(target=timer, args=(program_dict,))
    #always = mp.Process(target=always_display, args=(program_dict, name, roll))
    #timing.start()
    #always.start()
    #always.join()
    #file_handling(program_dict)
    counter = 1
    while counter<=3:
        always_display(program_dict, name, roll)
        display_and_get_ans(program_dict)
        #clear()
        time.sleep(1)
        counter += 1
    #timing.join()
    print(ans_dict)
    print(marks_dict)
    

