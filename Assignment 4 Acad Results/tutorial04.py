import numpy as np 
import pandas as pd 
import os,shutil

# spi calculation

def spi(credits, grades):
    gra = {"AA":10, "AB":9, "BB":8, "BC":7, "CC":6, "CD":5, "DD":4, "F":0, "I":0}
    weighted_sum = 0
    for x,y in zip(credits, grades):
        weighted_sum += (x*gra[y])

    return round((weighted_sum/sum(credits)),2)

# cpi calculation

def cpi(credits,spi_li):
    weighted_sum = 0
    for x,y in zip(credits,spi_li):
        weighted_sum += (x*y)
    return round((weighted_sum/sum(credits)),2)

# Deleting previously created grades folder

def del_previous_grades_folder():
    if os.path.exists("./grades"):
        shutil.rmtree("./grades")
    else:
        pass


del_previous_grades_folder()

#creating my grades folder

if os.path.exists("./grades"):
    pass
else:
    os.makedirs("./grades")


header1 = ["sub_code", "total_credits", "sub_type", "credit_obtained", "sem", "roll"]
headera = ["Subject", "Credits", "Type", "Grade", "Sem"]
cols = ["sub_code", "total_credits", "sub_type", "credit_obtained", "sem"]
df = pd.read_csv("acad_res_stud_grades.csv", usecols=header1)
misc_df = pd.read_csv("acad_res_stud_grades.csv")
rollnums = list(df["roll"].unique())


basepath = "./grades"
gra = {"AA":10, "AB":9, "BB":8, "BC":7, "CC":6, "CD":5, "DD":4, "F":0, "I":0}
for roll_num in rollnums:
    # checking whether roll_num is null or nan
    try:
        if np.isnan(roll_num) == True:
            misc_data = misc_df[pd.isnull(misc_df["roll"])]
            if(os.path.exists(os.path.join(basepath,"misc.csv"))):
                misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False, header=False)
            else:
                misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False)
            # since this roll number sent to misc we should not process the next try except , so continue is used
            continue
        else:
            pass
    except:
        pass

    temp = df[df["roll"] == roll_num]
    temp.drop("roll", axis=1)
    # checking whether any cell has null or nan value
    try:
        if len(temp.columns[temp.isnull().any()]) >0:
            #misc file
            misc_data = misc_df[misc_df["roll"] == roll_num]
            if(os.path.exists(os.path.join(basepath,"misc.csv"))):
                misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False, header=False)
            else:
                misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False)
            # since this roll number sent to misc we should not process the next try except , so continue is used
            continue
        else:
            pass
    except:
        pass


    try:
        if(set(list(temp["credit_obtained"].unique())).issubset(list(gra.keys())) and list(sorted(temp["sem"].unique())) == list(range(1,1+max(list(temp["sem"].unique()))))):
            
            #individual file
            filename = roll_num + "_individual.csv"
            with open(os.path.join(basepath,filename), "a+") as file:
                start = "Roll: {}".format(roll_num)
                info = "Semester Wise Details"
                start = [start,"", "", "", ""]
                info = [info,"", "", "", ""]
                start = pd.DataFrame(start).transpose()
                info = pd.DataFrame(info).transpose()
                start.to_csv(file, header=False, index=False)
                info.to_csv(file, header=False, index=False)
                temp.to_csv(file, index=False, columns=cols, header=headera)
            
            #overall file
            filename = roll_num + "_overall.csv"
            with open(os.path.join(basepath,filename), "a+") as file:
                li = list(temp["sem"].unique())
                sem_li = list()
                sem_credits_li = list()
                sem_credits_cleared_li = list()
                sem_spi_li = list()
                total_credits_li = list()
                sem_cpi_li = list()
                for semester in li:
                    sem_res = temp[temp["sem"] == semester]
                    sem_li.append(semester)
                    sem_credits_li.append(sem_res["total_credits"].sum())
                    sem_credits_cleared_li.append(sem_credits_li)
                    sem_spi_li.append(spi(list(sem_res["total_credits"]), list(sem_res["credit_obtained"])))
                    total_credits_li.append(sum(sem_credits_li))
                    if (len(sem_cpi_li) == 0):
                        sem_cpi_li.append(sem_spi_li[0])
                    else:
                        sem_cpi_li.append(cpi(sem_credits_li, sem_spi_li))

                dictionary = {"Semester": sem_li, "Semester Credits": sem_credits_li, "Semester Credits Cleared": sem_credits_li, "SPI": sem_spi_li, "Total Credits": total_credits_li, "Total Credits Cleared": total_credits_li, "CPI": sem_cpi_li}
                results = pd.DataFrame.from_dict(dictionary)
                start = "Roll: {}".format(roll_num)
                start = [start,"", "", "", "", "", ""]
                start = pd.DataFrame(start).transpose()
                start.to_csv(file, header=False, index=False)
                results.to_csv(file, index=False)
        else:
            #misc file
            misc_data = misc_df[misc_df["roll"] == roll_num]
            if(os.path.exists(os.path.join(basepath,"misc.csv"))):
                misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False, header=False)
            else:
                misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False)
    except:
        #misc file
        misc_data = misc_df[misc_df["roll"] == roll_num]
        if(os.path.exists(os.path.join(basepath,"misc.csv"))):
            misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False, header=False)
        else:
            misc_data.to_csv(os.path.join(basepath,"misc.csv"), mode="a+", index=False) 


