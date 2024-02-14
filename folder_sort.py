import os
from pprint import pprint

print(os.getcwd())

os.chdir("/home/wethinkcode/Downloads")
print(os.getcwd())
# dirlist = 
pprint(os.listdir("submission_001-accounting"))