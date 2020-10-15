import csv,os,re,datetime,shutil

def del_create_analytics_folder():
    if(os.path.exists("./analytics")):
        shutil.rmtree("./analytics")
    else:
        pass


def course():
    # Read csv and process
    del_create_analytics_folder()
    if(os.path.exists("./analytics")):
        shutil.rmtree("./analytics")
    else:
        pass
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]


    if(os.path.exists("./analytics/course")):
        pass
    else:
        os.makedirs("./analytics/course")

    base_path = "./analytics/course"
    for row in lines:
        if(bool(re.match('^[A-Z]+$',row["id"][4:6])) and len(row["id"]) == 8 and bool(re.match('^[0-9]+$',row["id"][0:2])) and bool(re.match('^[0-9]+$',row["id"][6:8]))):
            bcode = row["id"][4:6]
            if(os.path.exists(os.path.join(base_path,bcode.lower()))):
                pass
            else:
                os.makedirs(os.path.join(base_path,bcode.lower()))
            if(row["id"][2:4] == "01"):
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"btech"))):
                    pass
                else:
                    os.makedirs(os.path.join(base_path,bcode.lower(),"btech"))
                filename = row["id"][0:2] + "_" + bcode.lower() + "_btech.csv"
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"btech",filename))):
                    with open(os.path.join(base_path,bcode.lower(),"btech",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,bcode.lower(),"btech",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif(row["id"][2:4] == "11"):
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"mtech"))):
                    pass
                else:
                    os.makedirs(os.path.join(base_path,bcode.lower(),"mtech"))
                filename = row["id"][0:2] + "_" + bcode.lower() + "_mtech.csv"
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"mtech",filename))):
                    with open(os.path.join(base_path,bcode.lower(),"mtech",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,bcode.lower(),"mtech",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif(row["id"][2:4] == "12"):
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"msc"))):
                    pass
                else:
                    os.makedirs(os.path.join(base_path,bcode.lower(),"msc"))
                filename = row["id"][0:2] + "_" + bcode.lower() + "_msc.csv"
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"msc",filename))):
                    with open(os.path.join(base_path,bcode.lower(),"msc",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,bcode.lower(),"msc",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif(row["id"][2:4] == "21"):
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"phd"))):
                    pass
                else:
                    os.makedirs(os.path.join(base_path,bcode.lower(),"phd"))
                filename = row["id"][0:2] + "_" + bcode.lower()+ "_phd.csv"
                if(os.path.exists(os.path.join(base_path,bcode.lower(),"phd",filename))):
                    with open(os.path.join(base_path,bcode.lower(),"phd",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,bcode.lower(),"phd",filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            else:
                filename = "misc.csv"
                if(os.path.exists(os.path.join(base_path,filename))):
                    with open(os.path.join(base_path,filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,filename),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
        else:
            filename = "misc.csv"
            if(os.path.exists(os.path.join(base_path,filename))):
                with open(os.path.join(base_path,filename),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,filename),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)



def country():
    # Read csv and process
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]

    if(os.path.exists("./analytics/country")):
        pass
    else:
        os.makedirs("./analytics/country")

    base_path = "./analytics/country"
    for row in lines:
        if(row["country"] != ""):
            cinfo = row["country"]
            if(os.path.exists(os.path.join(base_path,cinfo.lower()+".csv"))):
                with open(os.path.join(base_path,cinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,cinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)
        else:
            cinfo = "misc"
            if(os.path.exists(os.path.join(base_path,cinfo.lower()+".csv"))):
                with open(os.path.join(base_path,cinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,cinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)


def email_domain_extract():
    # Read csv and process
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]

    if(os.path.exists("./analytics/email_domain")):
        pass
    else:
        os.makedirs("./analytics/email_domain")

    base_path = "./analytics/email_domain"
    for row in lines:
        einfo = row["email"].split("@")
        einfo = einfo[1].split(".")
        einfo = einfo[0]
        if(einfo != ""):
            if(os.path.exists(os.path.join(base_path,einfo.lower()+".csv"))):
                with open(os.path.join(base_path,einfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,einfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)
        else:
            ginfo = "misc"
            if(os.path.exists(os.path.join(base_path,einfo.lower()+".csv"))):
                with open(os.path.join(base_path,binfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,einfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)


def gender():
    # Read csv and process
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]

    if(os.path.exists("./analytics/gender")):
        pass
    else:
        os.makedirs("./analytics/gender")

    base_path = "./analytics/gender"
    for row in lines:
        if(row["gender"] != ""):
            ginfo = row["gender"]
            if(os.path.exists(os.path.join(base_path,ginfo.lower()+".csv"))):
                with open(os.path.join(base_path,ginfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,ginfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)
        else:
            ginfo = "misc"
            if(os.path.exists(os.path.join(base_path,ginfo.lower()+".csv"))):
                with open(os.path.join(base_path,ginfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,ginfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()



def dob():
    # Read csv and process
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]

    if(os.path.exists("./analytics/dob")):
        pass
    else:
        os.makedirs("./analytics/dob")

    base_path = "./analytics/dob"
    for row in lines:
        if(row["dob"] != ""):
            dinfo = row["dob"]
            if((datetime.datetime.strptime(dinfo,"%d-%m-%Y") >= datetime.datetime.strptime("01-01-1995","%d-%m-%Y")) and (datetime.datetime.strptime(dinfo,"%d-%m-%Y") <= datetime.datetime.strptime("31-12-1999","%d-%m-%Y"))):
                if(os.path.exists(os.path.join(base_path,"bday_1995_1999.csv"))):
                    with open(os.path.join(base_path,"bday_1995_1999.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,"bday_1995_1999.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif((datetime.datetime.strptime(dinfo,"%d-%m-%Y") >= datetime.datetime.strptime("01-01-2000","%d-%m-%Y")) and (datetime.datetime.strptime(dinfo,"%d-%m-%Y") <= datetime.datetime.strptime("31-12-2004","%d-%m-%Y"))):
                if(os.path.exists(os.path.join(base_path,"bday_2000_2004.csv"))):
                    with open(os.path.join(base_path,"bday_2000_2004.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,"bday_2000_2004.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif((datetime.datetime.strptime(dinfo,"%d-%m-%Y") >= datetime.datetime.strptime("01-01-2005","%d-%m-%Y")) and (datetime.datetime.strptime(dinfo,"%d-%m-%Y") <= datetime.datetime.strptime("31-12-2009","%d-%m-%Y"))):
                if(os.path.exists(os.path.join(base_path,"bday_2005_2009.csv"))):
                    with open(os.path.join(base_path,"bday_2005_2009.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,"bday_2005_2009.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif((datetime.datetime.strptime(dinfo,"%d-%m-%Y") >= datetime.datetime.strptime("01-01-2010","%d-%m-%Y")) and (datetime.datetime.strptime(dinfo,"%d-%m-%Y") <= datetime.datetime.strptime("31-12-2014","%d-%m-%Y"))):
                if(os.path.exists(os.path.join(base_path,"bday_2010_2014.csv"))):
                    with open(os.path.join(base_path,"bday_2010_2014.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,"bday_2010_2014.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            elif((datetime.datetime.strptime(dinfo,"%d-%m-%Y") >= datetime.datetime.strptime("01-01-2015","%d-%m-%Y")) and (datetime.datetime.strptime(dinfo,"%d-%m-%Y") <= datetime.datetime.strptime("31-12-2020","%d-%m-%Y"))):
                if(os.path.exists(os.path.join(base_path,"bday_2015_2020.csv"))):
                    with open(os.path.join(base_path,"bday_2015_2020.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,"bday_2015_2020.csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
            else:
                ginfo = "misc"
                if(os.path.exists(os.path.join(base_path,sinfo.lower()+".csv"))):
                    with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writerow(row)
                else:
                    with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                        header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                        writer.writerow(row)
        else:
            ginfo = "misc"
            if(os.path.exists(os.path.join(base_path,sinfo.lower()+".csv"))):
                with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)


def state():
    # Read csv and process
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]

    if(os.path.exists("./analytics/state")):
        pass
    else:
        os.makedirs("./analytics/state")

    base_path = "./analytics/state"
    for row in lines:
        if(row["state"] != ""):
            sinfo = row["state"]
            if(os.path.exists(os.path.join(base_path,sinfo.lower()+".csv"))):
                with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)
        else:
            ginfo = "misc"
            if(os.path.exists(os.path.join(base_path,sinfo.lower()+".csv"))):
                with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,sinfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)


def blood_group():
    # Read csv and process
    with open('studentinfo_cs384.csv') as f:
        reader = csv.DictReader(f)
        lines = [dict(row) for row in reader]

    if(os.path.exists("./analytics/blood_group")):
        pass
    else:
        os.makedirs("./analytics/blood_group")

    base_path = "./analytics/blood_group"
    for row in lines:
        if(row["blood_group"] != ""):
            binfo = row["blood_group"]
            if(os.path.exists(os.path.join(base_path,binfo.lower()+".csv"))):
                with open(os.path.join(base_path,binfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,binfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)
        else:
            ginfo = "misc"
            if(os.path.exists(os.path.join(base_path,binfo.lower()+".csv"))):
                with open(os.path.join(base_path,binfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
            else:
                with open(os.path.join(base_path,binfo.lower()+".csv"),"a+") as file:
                    header = ["id","full_name","country","email","gender","dob","blood_group","state"]
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writeheader()
                    writer.writerow(row)



# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass