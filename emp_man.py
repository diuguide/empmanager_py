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

todd = Employee("Todd", 34, "Boise", 18)

print(todd)
