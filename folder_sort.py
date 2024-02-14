import os
import sys
import shutil #allows us to delete a directory that is not empty
from pprint import pprint

print(os.getcwd())

os.chdir("/home/wethinkcode/Downloads") #make this path dynamic for future use 
"""now we want to analyse the different extentions of differnt files and check whether somesthing is a file or a folder"""
check = os.listdir()


for i in check:
    dotfind = i.rfind(".")
    # print(dotfind)
    if i[dotfind::] == ".zip":
        print(i)
        
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