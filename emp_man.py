print("Welcome to my Python Employee Manager")

#Class for all employees (this will be the parent class of all employees)
class Employee:
    def __init__(self, name, age, location, tenure_years):
        self.name = name
        self.age = age
        self.location = location
        self.tenure_years = tenure_years
    def __repr__(self):
        return "{name} is {age} years old.  Located in {location} and has worked for the company for {tenure_years} years!".format(name=self.name, age=self.age, location=self.location, tenure_years=self.tenure_years)

class CEO(Employee):
    wage = 100000
    vacation_days = 30

class Manager(Employee):
    wage = 75000
    vacation_days = 21

class Programmer(Employee):
    wage = 65000
    vacation_days = 14

class Intern(Employee):
    wage = 45000
    vacation_days = 7

#Empty dictionary for storing employees
employee_roster = {}

#functions to create employees
def enroll_ceo():
    print("ENROLL CEO")
    print("==========")
    name = input("Name:: ")
    age = input("Age:: ")
    location = input("Current location:: ")
    tenure_years = input("Years working:: ")
    return CEO(name, age, location, tenure_years)
    
#Query user for the employee to input
print("Please pick the type of employee to enroll:")
emp_list = ["1)CEO","2)Manager", "3)Programmer", "4)Intern"]

#list out choices
for role in emp_list:
    print(role)

#ask for number choice
role_input = input()
print(role_input)
if int(role_input) == 1:
    print("Enroll CEO")
    new_ceo = enroll_ceo()








