#creating sum of all the expenses in a list.

#creatinglist of expenses this week
expenses = [10.23, 8, 45, 12.5, 30.24, 50, 43.30]

summ = 0

for expense in expenses:
    summ = summ + expense

print("The total expense you spent this week is $", round(summ, 2), sep="")
# round(summ, 2) -> this changes 199.26999999999998 to 199.27, it rounds the number to 2 decimal places.)


##another way

expenses = [10.23, 8, 45, 12.5, 30.24, 50, 43.30]

total = sum(expenses)
print("The total expense you spent this week is $", total, sep="")