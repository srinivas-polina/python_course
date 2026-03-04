#often we see syntax errors caused by tapos in our code, and the pyhton interpreter comes upon one of those typos, it doen't know what we meant to do.
#Exceptions occur when the syntax is correct.
#so the python interpreter knows what we were trying to do, but the operation we were trying to do threw an error.

#one way of fixing an exception is catching it in a try/except block.

from ast import With


acronyms = {
    "LOL" : "Laugh Out Loud",
    "IDK" : "I don't Know",
    "TBH" : "To Be Honest"
}

try:
    definition = acronyms["BTW"]
    print(definition)
except:
    print("The Key does not exist")
finally:
    print("The acronyms we have defined are: ")
    for i in acronyms:
        print(i, ":", acronyms[i])

#the format of a try/except block is very similar to an if statement.

#try/except in Python is used to handle errors without stopping and crashing the program when an error occurs in the middle of the program.
#if we dont use try/except, the program will crash and stop running when it encounters an error, but with try/except, we can catch the error and continue running the program.
#Normally, if Python finds an error, the program crashes and stops running.
#With try/except, Python can catch the error and continue running.
#try:
    # code that might cause an error
#except:
    # code that runs if an error happens
#the finally keyword can be used after try/except blocks to run any code when thr tey/except block is finally done, regradless of whether an error occured or not.
#the fially keyword can be used to close objects or clean up resources.

#Raising exceptions
#we can Raise an error means intentionally creating an error in your program when something is wrong.

#Example : 1
age = -5

if age < 0:
    raise ValueError("Age Cannot be negative")

#Example: 2
def remainder_divison(a, b):
    if b == 0:
        raise ZeroDivisionError
    result = a//b
    remainder = a%b
    print(a, "/", b, "is", result, "remaindder", remainder)

#main program
remainder_divison(10, 0)

#Custom Exceptions

def remainder_divison(a, b):
    if b == 0:
        raise Exception("Cannot divide by Zero")
    result = a//b
    remainder = a%b
    print(a, "/", b, "is", result, "remaindder", remainder)

#main program
remainder_divison(10, 0)


