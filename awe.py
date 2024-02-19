import os 
from pprint import pprint
# print(os.getcwd())
# pprint(dir(os))
def modified_ext_directory(extensions_list)-> str:
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


lisst = ["jpg","mp4"]


print(modified_ext_directory(lisst))