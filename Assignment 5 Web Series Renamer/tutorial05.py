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
    try:
        season_pad = int(input())
        episode_pad = int(input())
        basepath = "./Subtitles"
        folder_path = os.path.join(basepath, folder_name)
        files = os.listdir(folder_path)
        for file in files:
            split_file = file.split('-')
            series_name = split_file[0]
            middle_split = split_file[1].split('x')
            middle_split = [ x.strip() for x in middle_split]
            season_num = middle_split[0]
            season_num = str(int(season_num))
            if len(split_file) > 3 and split_file[2].strip().isdigit():
                episode_num = str(int(middle_split[1])).zfill(episode_pad) + "-" + str(int(split_file[2].strip())).zfill(episode_pad)
                end_split = split_file[3].split('.')
                episode_name = end_split[0]
                episode_name = episode_name.strip()
                extension = file.split('.')[-1]
                newname = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num + " - " + episode_name + "." + extension
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))   

            else:
                episode_num = middle_split[1]
                episode_num = str(int(episode_num))
                end_split = split_file[2].split('.')
                episode_name = end_split[0]
                episode_name = episode_name.strip()
                extension = file.split('.')[-1]

                newname = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num.zfill(episode_pad) + " - " + episode_name + "." + extension
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))
    except:
        pass


def rename_Sherlock(folder_name):
    try:
        season_pad = int(input())
        episode_pad = int(input())
        basepath = "./Subtitles"
        folder_path = os.path.join(basepath, folder_name)
        files = os.listdir(folder_path)
        for file in files:
            split_file = file.split('.')
            series_name = split_file[0]
            extension = split_file[-1]
            list_of_all_numbers_in_filename = re.findall('[0-9]+',file)
            season_num = list_of_all_numbers_in_filename[0]
            season_num = str(int(season_num))
            episode_num = list_of_all_numbers_in_filename[1]
            episode_num = str(int(episode_num))
            newname = series_name + " - Season " + season_num.zfill(episode_pad) + " - " + "Episode " + episode_num.zfill(episode_pad) + "." + extension
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))
    except:
        pass


def rename_Suits(folder_name):
    try:
        season_pad = int(input())
        episode_pad = int(input())
        basepath = "./Subtitles"
        folder_path = os.path.join(basepath, folder_name)
        files = os.listdir(folder_path)
        for file in files:
            split_file = file.split('-')
            series_name = split_file[0]
            middle_split = split_file[1].split('x')
            middle_split = [ x.strip() for x in middle_split]
            season_num = middle_split[0]
            season_num = str(int(season_num))
            if len(split_file) > 3 and split_file[2].strip().isdigit():
                episode_num = str(int(middle_split[1])).zfill(episode_pad) + "-" + str(int(split_file[2].strip())).zfill(episode_pad)
                end_split = split_file[3].split('.')
                episode_name = end_split[0]
                episode_name = episode_name.strip()
                extension = file.split('.')[-1]
                newname = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num + " - " + episode_name + "." + extension
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))   

            else:
                episode_num = middle_split[1]
                episode_num = str(int(episode_num))
                end_split = split_file[2].split('.')
                episode_name = end_split[0]
                episode_name = episode_name.strip()
                extension = file.split('.')[-1]

                newname = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num.zfill(episode_pad) + " - " + episode_name + "." + extension
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))
    except:
        pass

def rename_How_I_Met_Your_Mother(folder_name):
    try:
        season_pad = int(input())
        episode_pad = int(input())
        basepath = "./Subtitles"
        folder_path = os.path.join(basepath, folder_name)
        files = os.listdir(folder_path)
        for file in files:
            split_file = file.split('-')
            series_name = split_file[0]
            middle_split = split_file[1].split('x')
            middle_split = [ x.strip() for x in middle_split]
            season_num = middle_split[0]
            season_num = str(int(season_num))
            if len(split_file) > 3 and split_file[2].strip().isdigit():
                episode_num = str(int(middle_split[1])).zfill(episode_pad) + "-" + str(int(split_file[2].strip())).zfill(episode_pad)
                end_split = split_file[3].split('.')
                episode_name = end_split[0]
                episode_name = episode_name.strip()
                extension = file.split('.')[-1]
                newname = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num + " - " + episode_name + "." + extension
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))   

            else:
                episode_num = middle_split[1]
                episode_num = str(int(episode_num))
                end_split = split_file[2].split('.')
                episode_name = end_split[0]
                episode_name = episode_name.strip()
                extension = file.split('.')[-1]

                newname = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num.zfill(episode_pad) + " - " + episode_name + "." + extension
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path,newname))
    except:
        pass

    
#folder_inp = input()

#folder_inp = "FIR"
#rename_FIR(folder_inp)

#folder_inp = "Game of Thrones"
#rename_Game_of_Thrones(folder_inp)

#folder_inp = "Sherlock"
#rename_Sherlock(folder_inp)

#folder_inp = "Suits"
#rename_Suits(folder_inp)

folder_inp = "How I Met Your Mother"
rename_How_I_Met_Your_Mother(folder_inp)