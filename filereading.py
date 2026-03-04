#pyhton has a special way of opening files using the with keyword that will make sure the file is closed when all of the file operations are finished, even if an exception is raised.
#the longer way of closing a file is using a try/finally block where the file operations are in the try block and then the file is closed in the finally block by calling file.close. 
file = open("acronyms.txt")
try:
    # Do file operations here
    pass
finally:
    file.close()

#Using with keyword is just a shortcut for doing the same thing and making sure our file is closed properly.
with open("acronyms.txt") as file:
    result = file.read()
    print(result)

#readline() method returns the next line of the file as a string
with open("acronyms.txt") as file:
    result = file.readline()
    print(result)


#readlines() method returns all lines of the file as a list of strings, then we can loop over this list to print each line of the file.
with open("acronyms.txt") as file:
    result = file.readlines()
    print(result)
    for i in result:
        print(i)

#we can also write above code in a shorter way by looping over the file object directly
with open("acronyms.txt") as file:
    for i in file:
        print(i)