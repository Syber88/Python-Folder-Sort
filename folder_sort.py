import os
import sys
import shutil #allows us to delete a directory that is not empty
from pprint import pprint

def get_username():
    pwd = os.getcwd() 
    dir_split = pwd.split("/")
    home = dir_split.index("home")
    try:  
        return dir_split[home+1]
    except:
        print("currently in the home directory")


def get_target_path(profile):
    return f"/home/{profile}/Downloads"


def change_directory(directory):
    os.chdir(directory)


def modified_ext_directory2(extension)-> str:
    categories = {
    "videos" : ["mp4","mkv"],
    "images" : ["jpeg","jpg","png","gif"],
    "docs"   : ["pdf","txt","doc", "docx", "odt","rtf","wpd"," wps"] ,  
    "compression" : ["zip","rar","7s","gz","tar"],
    "executables" : ["app", "bat", "bin", "cmd", "com", "exe", "vbs", "x86"],
    "programming files":  ["c", "cpp", "cs", "java", "js", "json", "py", "sql", "swift", "vb"]
    }

    for category, extension_raw in categories.items():
        if extension in extension_raw:
            return category
    

def modified_ext_directory1(extensions_list)-> set:
    ext_modded = []
    for extension in extensions_list:
        extension_extract = modified_ext_directory2(extension)
        ext_modded.append(extension_extract)
    return set(ext_modded)


def create_extension_directory(extensions):
    for extension_dir in extensions:
        if os.path.exists(extension_dir):
            print(f"Direcory {extension_dir} already exists" )
            return
        else:
            os.mkdir(f"{extension_dir}")
            print("i shoulda be making a directory", extension_dir)


def files_id() -> list[str]:
    """function to identify all the files in a directory
    return: list of all the available files in the directoroy"""
    dir_list = os.listdir()
    return [file for file in dir_list if os.path.isfile(file)]


def extension_id(file_list) -> list[str]:
    """function to identify different types of extensions used by files in directory"""
    return [os.path.splitext(file)[1][1:] for file in file_list]


def move_files(profile):
    os.chdir(f"/home/{profile}/Downloads")
    files = files_id()
    for file in files:
        ext = os.path.splitext(file)[1][1:]
        ext_hai = modified_ext_directory2(ext)
        destination = f"/home/{profile}/Downloads/{ext_hai}/{file}"


    # if os.path.exists(destination + f"{files}"):
    #     rename = files[:dotfind] + "_new"
    #     # shutil.move(source + f"{files}", destination_dir + f"{rename}")
    # else:
    #     shutil.move(source + f"{files}", destination_dir + f"{files}")

move_files(profile=get_username())

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