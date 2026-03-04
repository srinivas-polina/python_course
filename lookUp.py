# lets create a look up program by
#Asking the user what acronym they want to look up?
#Open the file
#Read each line of the file
  #check if current acronym matches the user's input acronym
     #print the definition of the acronym

look_up = input("What acronym do you want to look up?\n")
found = False
with open("acronyms.txt") as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print("Acronym not found in the file")
