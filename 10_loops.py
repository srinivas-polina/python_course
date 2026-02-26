# Loops using range()

#instead of entering all expenses at a time in the list like before demo, we can use a loop to ask the user to enter the expenses one by one and add them to the lsit.
total = 0
expenses = []

#asking how many expenses the user want to enter
num_expenses = int(input("How many expenses you want to enter? \n"))

for i  in range(num_expenses): #range(7) -> this will generate a sequence of numbers from 0 to 6, it will run the loop 7 times.
    expenses.append(float(input("Enter your expense: \n")))

total = sum(expenses)

print("The total expenses of this week is $", total, sep='')