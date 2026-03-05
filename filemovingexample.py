import os
#assigning the path of the original folder and the destination folder to variables.
folder_original = "C:/Users/polin/OneDrive/Desktop/"
folder_destination = "C:/Users/polin/OneDrive/Desktop/CleanedUp/"
#creating the destination folder if it does not exist already
os.mkdir(folder_destination)
#looping over all of the entries on the desktopfolder
entries = os.scandir(folder_original)
for entry in entries:
    #in order to move files, we need to create the absolute path of the original file and the destination file using os.path.jion() function.
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)
    #lets also check we are only moving files not directories
    if os.path.isfile(location_original):
         os.rename(location_original, location_destination)
         #finally we can move the files using os.rename


