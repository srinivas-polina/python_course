#In python we can have a container of containers.
#combing lists in lists is called a nested list,
#combing dictionaries in dictionaries is called a nested dictionaries.
#combing lists and dictionaries is called a nested data structure.

menus = [["Egg Sandwich","Bagel","Coffee"],
         ["BLT","PB&J","Turkey Sandwich"],
         ["Soup","Salad","Sapaghetti","Tacos"]]

print('Breakfast menu: \n',menus[0])
print('Lunch menu: \n', menus[1])
print('Dinner menu: \n', menus[2])

#getting an individual itemfrom inner list.
print(menus[0][0]) #Egg Sandwich
print(menus[1][1]) #PB&J
print(menus[2][3]) #Tacos

#instead of using lists of lists, we can use dictionaries with keys for the breakfast, lunch, and dinner lists.
#whic is littel more organised and easier to read.

menus = {
    "Breakfast" : ["Egg Sandwhich", "Bagel", "Coffee"],
    "Lunch" : ["BLT", "PB&J", "Turkey Sandwhich"],
    "Dinner" : ["Soup", "Salad", "Sapaghetti", "Tacos"]
}

print("Breakfast Menu:\t", menus["Breakfast"])
print("Lunch Menu:\t", menus["Lunch"])
print("Dinner Menu:\t", menus["Dinner"])

#we can also do using for loop to print the menu
for name, menu in menus.items():
    print(name, ":", menu)


##
person = {
    "name" : "John Doe",
    "age" : 30,
    "hobbies" : ["reading", "hiking", "cooking"],
    "education" : {
        "highschool" : "ABC High School",
        "college" : "XYZ University",
        "graduate" : "PQR Graduate school"
    },
    "contact" : {
        "email" : "john.doe@example.com",
        "phone" : "123-456-7890"
    }
}


print("The person Name is: ", person.get("name"), "\n his age is: ", person.get("age"), "\n his contact email is: ", person.get("contact").get("email"), "\n his conatct phone number is: ", person.get("contact").get("phone"), ".", sep ="")

