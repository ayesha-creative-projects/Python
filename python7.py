# pyhton 7: scope, str.format


# scope (local then global will print)
name = "spongbob" # global can use inside and outside

def display( ):
    name = "code" # local ony use inside
    print(name)

display()
print(name)

# *args → values packed in a tuple (u use this When you want a function to accept any number of values.)
def add(a, b):     # here it can't add more numbers
    print(a + b)

add(2, 3)          # example without args


def add(*args):    # example with args
    print(args)

add(1, 2, 3, 4)   # all values stored in tuple


def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add(1, 2, 3, 4, 5)

# **kwargs → values packed in a dictionary (u use it When you want to accept named values.)
def student_info(**kwargs):
    print(kwargs)

student_info(name="Spongbob", age=17, degree="water")  #Stored as a dictionary.


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="spongbob", city="ocean", hobby="swimming")


def info(*args, **kwargs):  # used args and kwargs together
    print("Args:", args)
    print("Kwargs:", kwargs)

info(1, 2, 3, name="Ayesha", age=17)


# str.format() is used to put values inside a string neatly.
# {} are placeholders
# .format() fills those placeholders

name = "SpongBob"
age = 17

print("My name is {} and I am {} years old.".format(name, age))
print("I love {} and {}.".format("Python", "Robots"))
print("I am {1} years old and my name is {0}.".format("Ayesha", 17))
# {0} → first value
# {1} → second value
print("My name is {name} and I study about {degree}.".format(
    name="SpongBob",
    degree="Water"
))
pi = 3.14159
print("Value of pi is {:.2f}".format(pi))
print("{:<10} | {:^10} | {:>10}".format("Left", "Center", "Right"))
print("{0} loves {1}. {0} studies {2}.".format("SpongBob", "swimming", "Water"))

city = "Lahore"
temp = 25
print("Temperature in {} is {}°C.".format(city, temp))