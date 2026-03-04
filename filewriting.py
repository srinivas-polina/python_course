#step need to do
#1. Ask the user what acronym they want to add to the file
#2. Ask the user for the definition of the acronym
#3. Open the file
#4. Write the new acronym and definition to the file  

acronym = input("What Acronym do you want to add? \n")
definition = input("what is the definition? \n")
#r is the default mode for opening a file, it stands for reading, w stands for writing, and a stands for appending.
#if we want to write to a file, we need to open in write mode but here the existing content of the file will be deleted, 
#in our case we just need to add a new acronym and definition to the file without deleting the exisiting content, so we will open the file in append mode.

with open("acronyms.txt", "a") as file:
    file.write(acronym+ "-" + definition + "\n")
