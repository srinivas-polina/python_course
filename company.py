#since we want our Companyclass to have access to the Employee class, we will need to import it.
from employee import Employee, SalaryEmployee, HourlyEmployee, CommisionEmployee

class Company():
    def __init__(self):
        self.employees = [] #creating an empty list to store the employees in the company.
        #since we have a list of employees, we want a way to add employess to that lsit.
    def add_employee(self, new_employee):
        self.employees.append(new_employee) #this method takse a new employee object as a argument and adds it to the employees list.

    def display_employees(self):
        print("Current Employees in the Company: ")
        for i in self.employees:
            print(i.fname, i.lname)
        print("____________________")
    def pay_employee(self):
        print("Paying Employees:")
        for i in self.employees:
            print("Paycheck for: ", i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():.2f}') #this will call the calculate paycheck method for each employee and print the amount in a formatted way with 2 decimal places.
            print("____________________")

def main():
    #creating a company object
    my_company = Company()

    employee1 = SalaryEmployee("John", "Smith", 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Lee", "Johnson", 25, 50)
    my_company.add_employee(employee2)
    employee3 = CommisionEmployee("Jane", "Williams", 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employee()

main()




