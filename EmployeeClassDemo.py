#creating a company class to manage and write their weekly paychecks.
#To do that , we will also need an employee class.

class Salary_Employee():
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52 #assuming the employee is paid weekly, we divide the annual salary by 52 to get the weekly paycheck.
    
#creating an employee object from the employee class
#emp1 = Employee("John", "Smith", 52000)

#Call method
#weekly_pay = emp1.calculate_paycheck()

#print("Employee", emp1.fname, emp1.lname)
#print("Weekly Paycheck: $", weekly_pay,sep="")

#now we can create a company class in another file.