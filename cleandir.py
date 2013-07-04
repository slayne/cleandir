#!/usr/bin/python3.3

import os
import re
import shutil

def checkName(realname, filename): return all(re.search(t, filename) for t in realname.lower().split())
def checkFormat(name,format): return any(re.search(t,name) for t in format)

#Go to the right directory
os.chdir("/directory/to/clean") #replace by your directory 
#Get all the files
allfiles=os.listdir(os.getcwd())

#video formats
videos=["mp4","avi","mkv"] #replace / add video formats
#archive formats
archives=["zip","rar"] #replace / add archives formats

#path for unsorted videos
video_path="/path/to/the/right/dir" #replace

#path for unsorted archives
archive_path="/path/to/the/right/dir" #replace

#List all the names and their associeted path, replace by yours
series={"name":"/path/to/the/right/dir",
        "name2":"/path/to/the/right/dir"}
        
#Normalize files
for name in allfiles:
    name=name.lower()
    
#sort series
for k in series:
    for f in allfiles:
        if checkName(k,f):
            print("moving",f)
            shutil.move(f,series[k])
            
        #sort other videos
        if checkFormat(f,videos):
            print("moving",f)
            shutil.move(f,video_path) 

        #sort archives 
        if checkFormat(f,archives):
            print("moving",f)
            shutil.move(f,archive_path) 
