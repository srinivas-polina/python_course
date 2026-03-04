#function for finding an acronym in a file
def find_acronym():
    look_up = input("What acronym do you want to look up?\n")
    found = False
    try:
        with open("acronyms.txt") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not Found")
        return

    if not found:
        print("Acronym not found in the file")

#function for adding an new acronym and definition to the file.
def add_acronym():
    acronym = input("What Acronym do you want to add? \n")
    definition = input("what is the definition? \n")
    with open("acronyms.txt", "a") as file:
        file.write(acronym+ "-" + definition + "\n")

#Main Program
def main():
    choice = input("Do you want to Find(F) or Add(A) an acronym? \n")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()

main()
