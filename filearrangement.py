import os
import shutil

desktop_path = os.path.expanduser("~\\Desktop")
print(desktop_path)
#creating a dictionary to store the folder names and the file extensions that belong in those folders.
folders = {
    "Images" : [".jpeg", ".jpg", ".png", ".gif"],
    "Documents" : [".doc", ".docx", ".pdf", ".txt"],
    "Archives" : [".zip", ".rar"]
}
#creating folders on the desktop if they do not exist already
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
   #print(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

#move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
   original_path = os.path.join(desktop_path, file_name)
   if os.path.isfile(original_path):
       for folder_name, extensions in folders.items():
           for extension in extensions:
               if file_name.endswith(extension):
                   destination_folder = os.path.join(desktop_path, folder_name)
                   shutil.move(original_path, destination_folder)