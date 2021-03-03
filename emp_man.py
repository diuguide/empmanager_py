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

def enroll_mngr():
    print("ENROLL MANAGER")
    print("==========")
    name = input("Name:: ")
    age = input("Age:: ")
    location = input("Current location:: ")
    tenure_years = input("Years working:: ")
    return Manager(name, age, location, tenure_years)

def enroll_prgmr():
    print("ENROLL PROGRAMMER")
    print("==========")
    name = input("Name:: ")
    age = input("Age:: ")
    location = input("Current location:: ")
    tenure_years = input("Years working:: ")
    return Programmer(name, age, location, tenure_years)

def enroll_int():
    print("ENROLL INTERN")
    print("==========")
    name = input("Name:: ")
    age = input("Age:: ")
    location = input("Current location:: ")
    tenure_years = input("Years working:: ")
    return Intern(name, age, location, tenure_years)
    
#Query user for the employee to input

emp_list = ["1)CEO","2)Manager", "3)Programmer", "4)Intern"]

#list out choices
for role in emp_list:
    print(role)

#ask for number choice
def get_user_input():
    print("Please pick the type of employee to enroll:")
    return input(">>>> ")

#Elseif to direct role_input
def create_employee(role_input):
    if int(role_input) == 1:
        new_ceo = enroll_ceo()
        print(new_ceo)
    elif int(role_input) == 2:
        new_mngr = enroll_mngr()
        print(new_mngr)
    elif int(role_input) == 3:
        new_prgmr = enroll_prgmr()
        print(new_prgmr)
    elif int(role_input) == 4:
        new_int = enroll_int()
        print(new_int)
    elif int(role_input) != len(range(1,5)):
        print("INPUT ERROR")

create_employee(get_user_input())
print("End of file: testing global config settings")







