

#Example 1 (Local Scope)
#Think of functions as mini programs
def greeting(name):
    print("Hello", name)

# Main Program
name = input("What is your Name? \n")
greeting(name)



# A function must be defined before it is called in a program.
# If you try to call a function before defining it, Python will raise an error.
#This means order of code execution matters in python. you must define a function before you can use it in your program.
# This is similar to variables — you must create (define) a variable
# before you try to use it.

# In programming, the order of code execution matters.
# Also, scope (local and global) matters because it determines
# where a variable can be accessed inside the program.
#A variable defined inside of a function is only avalible to be used inside of that function. This is called a local scope.
# it was like def greeting(name): here we defined a variable "name" inside the greeting function, and we can only use that variable inside that function,
#we cannot use that "name" variable outside the function like print(name) because it is not defined outside the function,it is only defined inside the function, so it will raise an error if we try to access it outside the function.

#if a variable is created inside the main program,then it is a global variable and has global scope, meaning it can be used anywhere even inside a funciton definition.

#Example 3 (Global  Scope)
def greeting():
    print("Hello", name)

name = input("What is your Name? \n")

greeting()


#using global variables can get messy.
#like above we are using the global variable "name"inside the greeting function, but what if we enter another name and save it to another vatrible like "name2" and then we want to use that "name2" variable inside the greeing function,
#we will have to change the name of the global variable "name" to "name2" inside the greeting function, and then we will have to change it back to "name" if we want to use it again, this can get messy and confusing, especially if we have a lot of global variables in our program.
#it work only like below but it is not a good practice, then the original "name" variable will be lost and we willonly have "name2" variable to use in the greeting function.
def greeting():
    print("Hello", name)

name = input("What is your Name? \n")

name2 = input("what is your Name? \n")
name = name2
greeting()

#but by using the local scope we can do like below
def greeting(name):
    print("Hello ", name)

name1 = input("What is your Name?  \n")
greeting(name1)

name2 = input("What is your name? \n")
greeting(name2)

#local scope allows us to reuse the same function with different variables without having to change the global variable name, and it also helps us to avoid confusion and messiness in our program, and it also help us to keep our code orgainizedand easy to read.

#there is two main reasons why we use functions in programming:
#1. Reusability: we can resuse a chunk of code over and over again like greeting function that we used same function with different variables without having to change the code inside the function, this is called reusability.
#2. Grouping code into logical units: we can group code into logical units like we can group all the code that is related to greeting into a function, this is called grouping code into logical units, and it helps us to keep our code organized and easy to read.
#Grouping Example:
#Example
def addition(x,y):
    return x + y

#as we can use functions to organise our code into logical units, So we can take this main body of the code below and put it inside a function called main()
#Main Function
def main(): #now all of this program code is contained inside of the main function. but if we want to run this program we have to call the main function at the end of the program after the functions are declared like below.
    num1 = float(input("Enter your 1st number: \n"))
    num2 = float(input("Enter your 2nd number: \n"))

    #calling the function

    result = addition(num1, num2)
    print("The result is: ", result)

main() #calling the main function to run the program
#now the code is orgainised into functions


