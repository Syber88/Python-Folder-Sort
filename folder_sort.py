import os
import sys
import shutil #allows us to delete a directory that is not empty
from pprint import pprint

pwd = os.getcwd()
print(pwd[:6])
os.chdir("/home/wethinkcode/Downloads") #make this path dynamic for future use 
"""now we want to analyse the different extentions of differnt files and check whether somesthing is a file or a folder"""
dir_list = os.listdir()

def create_extension_directory(extension):
    if os.path.exists(extension):
        return
    else:
        os.mkdir(f"{extension}")
        
def get_username():
    dir_split = pwd.split("/")
    user_profile_index = dir_split.index("home")
    return dir_split[user_profile_index]
     
    # for dir in dir_split:
    #     if dir == "home":
    #         home_index = 

"""isolate the current working direcrory using getcwd"""
for files in dir_list:
    if os.path.isfile(files):
        dotfind = files.rfind(".")
        if files[dotfind+1::] == "zip":
            create_extension_directory("zip") #having a function to create a directory
            #is unnecessary since shutil will automatically make one if it does not already exist
            source = f"/home/wethinkcode/Downloads/"
            destination_dir = f"/home/wethinkcode/Downloads/zip/"
            if os.path.exists(destination_dir + f"{files}"):
                rename = files[:dotfind] + "_new"
                shutil.move(source + f"{files}", destination_dir + f"{rename}")
            else:
                shutil.move(source + f"{files}", destination_dir + f"{files}")



            # print(i)
        
        #use rfind to find the last occurence of something 
        
        
        
# print(os.getcwd())
# dirlist = 
# os.mkdir("awepls")
# os.rename("awepls","anotherone") 
# os.remove("test.txt") 
# try:
#     os.rmdir("awe")
# except:
#     print("the directory is not empty")
    
# shutil.rmtree("awe")
# pprint(dir(os))

# pprint(check)