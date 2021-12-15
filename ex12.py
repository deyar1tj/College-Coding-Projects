# In-Class Assignment 12 - Review
# Author: Tristan Deyarmond

# Problem 1
# Given the following list, write Python code to remove all of the empty strings
# tuples, lists, and dictionaries as well as any instances of the null variable
# None and store the resulting list in a variable cleaned_list.
cluttered_list = [None, [], [1,2,3], "Hello world!", (), ""]
cleaned_list = [x for x in cluttered_list if x]
for x in cluttered_list:
    if x:
        print("true")
    else:
        print("false")


# Problem 2
# Write the Python code to declare a class Car that has the following decorated
# properties: make, model, year. Overriden the __str__ method to print out these
# attributes.
class Car:

def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

@property
def make(self):
    return self.__make

@make.setter
def make(self, make):
    self.__make = make

@property
def model(self):
    return self.__model

@model.setter
def model(self, model):
    self.__model = model

@property
def year(self):
    return self.__year

@year.setter
def year(self, year):
    self.__year = year

def __str__(self):
    return self.make + " " + self.model + " " + self.year

c = Car("Chevy", "Blazer", "2020")
print(c)

# Problem 3
# A user is asked to enter a year which is number and program tell whether it is a leap year or not.
# If the user enters a character like a-z, then a ValueError occurs. Use try-except to handle the exception.
try:

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
# Problem 4
# Given a list of mixed items, use a for loop to iterate through the list items.
# In each iteration, see if the current item of the list able to be divided by a numeric type variable.
# If an error occurs, catch it and print a small message.
a_list = [5, 'c', 20, 0, 40]
b = 15

for x in a_list:
    try:
        z = b / x
        print(z)
    except ZeroDivisionError:
        print("Can't divide by zero")
    except TypeError:
        print("Can't divide by a letter")
