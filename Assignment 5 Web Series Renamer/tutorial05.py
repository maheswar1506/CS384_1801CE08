import os,re

def rename_FIR(folder_name):
    try:
        season_pad = int(input())
        episode_pad = int(input())
        basepath = "./Subtitles"
        folder_path = os.path.join(basepath, folder_name)
        files = os.listdir(folder_path)
        for file in files:
            split_file = file.split('-')
            series_name = split_file[0]
            extension = file.split('.')[-1]
            list_of_all_numbers_in_filename = re.findall('[0-9]+',file)
            episode_num = list_of_all_numbers_in_filename[0]
            episode_num = str(int(episode_num))
            newname = series_name + "- Episode " + episode_num.zfill(episode_pad) + "." + extension
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname)) 
    except:
        pass

def rename_Game_of_Thrones(folder_name):
    pass

def rename_Sherlock(folder_name):
    pass


def rename_Suits(folder_name):
    pass

def rename_How_I_Met_Your_Mother(folder_name):
    pass

    
#folder_inp = input()

folder_inp = "FIR"
rename_FIR(folder_inp)
