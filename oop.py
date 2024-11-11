#Object Orientated Programming(OOP)

# It always has Classes and Objects/instance.
# A class always has properties/ attributes.
# Methods are items of the class.
# Objects come from a class. 
# An object takes on the properties of a class.

# Syntax of OOP
#1. Creating classes
#Cohort class and class names start with an upper case
#   name
#   description
#   start_date
#   end_date

class Cohort:
    name='Favour'
    description= 'Cohort 4'
    start_date='20th October'
    end_date='2026'
    
# print(Cohort)

#Within the cohort class, 
#add a constructor for the cohort class.(Read about constrcutors and objects/instances)
# add a method to the class that prints the cohort name and the total number of students.
# Create a new instance/Object of the cohort class.


# Adiing a constructor
class Cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name=name
        self.description= description
        self.start_date= start_date
        self.end_date= end_date
Cohort=Cohort('Favour', 'Cohort 4', '20th August', '2026')
print(Cohort.name)
print(Cohort.description)
print(Cohort.start_date)
print(Cohort.end_date)

# Adding a method
class Cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name=name
        self.description= description
        self.start_date= start_date
        self.end_date= end_date
    def total(self):
            print('The total number of students is 63' +  self.name)
Details=Cohort('Favour', 'Cohort 4', '20th August', '2026')
Details.total()

#New object for the class
class Cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name=name
        self.description= description
        self.start_date= start_date
        self.end_date= end_date
    def cohort_func(self):
        print(self.name, self.description, self.start_date, self.end_date)
class Subject(Cohort):
    def __init__(self, name, description, start_date, end_date):
        super().__init__(name, description, start_date, end_date)
        self.Subject = 'programming'
details = Subject('Favour','Cohort4','20th August','2026')
print(details.Subject)