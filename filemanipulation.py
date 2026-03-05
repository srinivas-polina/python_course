#python has several built-in modules for handling files
#os, shutil, and pathlib

#using some of the functionality in the os module that requires listing contents of a directory, making new directories, moving files and getting file attributes.

#lets say we currently have a mess of files in the desktop folder, 
#and we want to clean them up by moving those files to a new folder caleed cleanedUp on the desktop.

#steps to list out to create this program:
#1. create or make the folder CleanedUp/
#2. Then List files in the Desktop/ folder
#3. loop over othose each file in the Desktop/ folder
  #4. Move the file to the CleanedUp/ folder

#import os module, helps us by providing some functionality to interact with our operating system to make directories, list files, and move files.
import os

#making a new folder called CleanedUp by callin os.mkdir() method and passing the name of the folder we want to create as an argument.
os.mkdir("C:/Users/polin/OneDrive/Desktop/CleanedUp")

#if we want to list all of the entries in a directory, entries mean files and folders
#we can use the os.scandir()
folder = "c:/Users/polin/OneDrive/Desktop/"
entries = os.scandir(folder)
#this returns a iterator or pointer to a list of the file objects.
#we can loop over this list to print all of the entry names.
for entry in entries:
    print(entry.name)

#let edit our print statement to check if the entry is a file or a directory.
for entry in entries:
    if os.path.isfile(entry):
        print("File:", entry.name)
    elif os.path.isdir(entry):
        print("Directory:", entry.name)

#we can use the function os.path.join to create an absolute path from a path string and a file name.
#we can also use concatenation to create an absolute path by using + operater to combine the path string and the file name, 
#but usinh os.path.jion function can add any missing slashes or get rid of any extra for us.
#here we want to move the new.txt file from the desktop to the cleanedUP folder.

folder_original = "C:/Users/polin/OneDrive/Desktop/"
folder_new = "C:/Users/polin/OneDrive/Desktop/CleanedUp/"

location_original = os.path.join(folder_original, "new.txt")
location_destination = os.path.join(folder_new, "new.txt")

os.rename(location_original, location_destination)
