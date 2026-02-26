# List : A list is a python containers that can store anything we want, it is changeable, and it is ordered. we can use square brackets to create a list, and we can use the index to access the elements in the last. we can also use the built in functions to manipulate the list.
# Different types of lists:
# 1.List of strings = ["apple", "banana", "cherry"]
# 2.List of integers = [1, 2, 3, 4, 5]
# 3.List of mixed data types = ["apple", 1, 2.5, True]
# 4.List of lists = [[1, 2, 3], ["apple", "banana", "cherry"], [ True, False, None]]

#we are going to create a translation app for acronyms on the internet.

acronyms = ["LOL", "IDK", "SMH"]
word = "BFN"

#adding new element to list
acronyms.append("TBH") #calling the append method to add an element to the end of the list
acronyms.append("IMHO")

print(acronyms)

#removing or deleting an element from the list
acronyms.remove("TBH") #calling the remove method to remove an element from the list
#or
del acronyms[3] #removing an element from the list using the index  position of the element

print(acronyms)

#checking if an element in the list
if word in acronyms:
    print(word , "is in acronyms")
else:
    print(word, "is not in acronyms")

#printing each acronym in the list
for acronym in acronyms:
    print(acronym)