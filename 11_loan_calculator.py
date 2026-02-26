#creating a loan calculator.
#this will caclulate how much of a loan or a mortagage we  paid  off after a given number of months.

#getting the  details of the loan from the user.
money_owed = float(input("How much money do you owe, in dollars? \n"))
apr = float(input("what is your annual percentage rate of the loan ? \n"))
monthly_payment = float(input("How much do you want to pay each month in dollars? \n"))
months = int(input("How many months do you want to see the results for? \n"))

monthly_rate = apr/100/12 #divide apr by 100 to convert it to a decimal, then divide by 12 to get the monthly interest rate.

for i in range(months):
    #calculating frist month's interest and add it to the amount owed
    interest_paid = money_owed * monthly_rate
    #add in interest
    money_owed = money_owed + interest_paid
    
    if (money_owed - monthly_payment < 0):
        print("You paid off the loan!")
        print("you paid off the loan in", i+1, "months!")
        break
    #make the payment
    money_owed = money_owed - monthly_payment

    print("paid", monthly_payment, "of which", interest_paid, "was interest")
    print("Now, you owe", money_owed)