import os
import sys
import shutil #allows us to delete a directory that is not empty
from pprint import pprint

def get_username():
    pwd = os.getcwd() #does not matter which directory you are in, but what if you're in the home directory. sort that out later 
    dir_split = pwd.split("/")
    home = dir_split.index("home")
    try:  
        return dir_split[home+1]
    except:
        print("currently in the home directory") #remove once terminal work and picking is once complete


def get_target_path(profile):
    #get profile name from get_username and pass result onto change_directory. Downloads for now
    return f"/home/{profile}/Downloads"


def change_directory(directory):
    # profile = get_username()
    os.chdir(directory) #make this path dynamic for future use 

def modified_ext_directory2(extension)-> str:
    videos = ["mp4","mkv"]
    images = ["jpeg","jpg","png","gif"]
    docs   = ["pdf","txt"]   
    if extension in videos:
        return "videos"
    elif extension in images:
        return "images"
    elif extension in docs:
        return "documents"
    else: 
        return extension
    

def modified_ext_directory1(extensions_list)-> set:
    videos = ["mp4","mkv"]
    images = ["jpeg","jpg","png","gif"]
    docs   = ["pdf","txt"]
    hai = []
    for extension in extensions_list:
        if extension in videos: 
            hai.append("videos")
        elif extension in images:
            hai.append("images")
        elif extension in docs:
            hai.append("documents")
        else: 
            hai += extension
    return set(hai)

    #parameter fed from mod ext dir
def create_extension_directory(extensions):
    for extension_dir in extensions:
        if os.path.exists(extension_dir):
            print(f"Direcory {extension_dir} already exists" )
            #get extensions from extension_id
            return
        else:
            os.mkdir(f"{extension_dir}")
            # print(f"directory made {extension_dir}")
            print("i shoulda be making a directory", extension_dir)


"""isolate the current working direcrory using getcwd"""
"""break down the code below into functions"""
"""get a way to breakdown the code into separate functions"""
"""function names will be, extensions identifier, extension move"""
def files_id() -> list[str]:
    """function to identify all the files in a directory
    return: list of all the available files in the directoroy"""
    dir_list = os.listdir()
    return [file for file in dir_list if os.path.isfile(file)]


def extension_id(file_list) -> set:
    """function to identify different typesp of extensions used by files in directory"""
    return [os.path.splitext(file)[1][1:] for file in file_list]

def move_files(profile):
    # source = get_target_path(profile)
    os.chdir(f"/home/{profile}/Downloads")
    files = files_id()
    for file in files:
        ext = os.path.splitext(file)[1][1:]
        ext_hai = modified_ext_directory2(ext)
        destination = f"/home/{profile}/Downloads/{ext_hai}/{file}"
    
        print("ext--", ext)
        print()
        print("destination---", destination)
        print("=============================================")
    print(file)
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