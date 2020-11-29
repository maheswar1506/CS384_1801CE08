import os, shutil, math
import numpy as np 
import pandas as pd
from operator import itemgetter

if os.path.exists("./groups"):
    shutil.rmtree("./groups")

def group_allocation(filename, number_of_groups):
    # Entire Logic 
    # You can add more functions, but in the test case, we will only call the group_allocation() method,
    if os.path.exists("./groups"):
        pass
    else:
        os.makedirs("./groups")
    basepath = "./groups"

    df = pd.read_csv(filename)

    # strength.csv
    unq_branches = list(df["Roll"])
    unq_branches = [branch[4:6].upper() for branch in unq_branches]
    unq_branches = list(set(unq_branches))
    strength = {branch : 0 for branch in unq_branches}
    for roll in list(df["Roll"]):
        strength[roll[4:6]] += 1
    strength = sorted(strength.items(), key=itemgetter(0))
    strength = sorted(strength, key=itemgetter(1), reverse=True)
    strength = pd.DataFrame(strength, columns=["BRANCH_CODE", "STRENGTH"])
    strength.to_csv(os.path.join(basepath, "branch_strength.csv"), mode="a+", index=False)

    # branch files
    branch_df = pd.read_csv(os.path.join(basepath, "branch_strength.csv"))
    branch_copy = list(branch_df["BRANCH_CODE"])
    for branch in branch_copy:
        data = df[df["Roll"].str[4:6] == branch]
        file = branch + ".csv"
        data = data.sort_values(by="Roll")
        data.to_csv(os.path.join(basepath,file), mode="a+", index=False)

    # Group files
    branch_dict = {code: strgh for code, strgh in zip(list(branch_df["BRANCH_CODE"]), list(branch_df["STRENGTH"]))}
    group_dict = {branch : {"Group_G{}.csv".format(str(i).zfill(2)) : math.floor(branch_dict[branch]/number_of_groups) for i in range(1, number_of_groups+1)} for branch in branch_dict.keys()}
    left_dict = {code: strgh%number_of_groups for code, strgh in zip(list(branch_df["BRANCH_CODE"]), list(branch_df["STRENGTH"]))}
    left_li = [key for key,value in left_dict.items() for j in range(value)]
    app_li = [left_li[i:i+number_of_groups] for i in range(0, len(left_li), number_of_groups)]
    group_li = ["Group_G{}.csv".format(str(i).zfill(2)) for i in range(1, number_of_groups+1)]
    for lovely in app_li:
        for i in range(len(lovely)):
            group_dict[lovely[i]][group_li[i]] += 1
    stats_dict = group_dict.copy()
    grp_files = [file+".csv" for file in group_dict.keys()]
    grp_files_df = {}
    for file in grp_files:
        love = pd.read_csv(os.path.join(basepath, file))
        grp_files_df[file[:-4]] = love
    for code, code_val in group_dict.items():
        for grp, grp_val in code_val.items():
            if os.path.exists(os.path.join(basepath, grp)):
                grp_files_df[code].iloc[:grp_val].to_csv(os.path.join(basepath, grp), mode="a+", index=False, header=False)
                grp_files_df[code] = grp_files_df[code].iloc[grp_val:]
            else:
                grp_files_df[code].iloc[:grp_val].to_csv(os.path.join(basepath, grp), mode="a+", index=False)
                grp_files_df[code] = grp_files_df[code].iloc[grp_val:]   

    # stats file
    temp_dict = {"Group_G{}.csv".format(str(i).zfill(2)) : 0 for i in range(1, number_of_groups+1)}
    for code, code_val in stats_dict.items():
        for grp, grp_val in code_val.items():
            temp_dict[grp] += grp_val
    stats_df = pd.DataFrame(stats_dict).reset_index()
    stats_df.rename(columns={"index": "group"}, inplace=True)
    stats_df.insert(1,"total", temp_dict.values())
    stats_df.to_csv(os.path.join(basepath, "stats_grouping.csv"), mode="a+", index=False)


filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)