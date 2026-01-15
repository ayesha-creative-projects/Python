# python 1: variables, typecasting, input

# This is my first Python program
print("I like pizza!")
print("I am learning to code")

# variables (string, integer, float, boolean)
first_name = 'Python'  #string
age = 3             #integer
price = 3.99        #float
is_study = True     #boolean

print(f"My name is {first_name}") # 1
print(f"my age is {age}")         # 2
print(f"the price is ${price}")   # 3
print(f"Did i studied for Python?: {is_study}")  # 4

# 5
if is_study:
    print("you did study")
else:
    print("you did NOT study")

# 6
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#typecasting (conversion of datatypes)
name = " Python"
age = 13
gpa = 3.2
is_student = True

# 1
print(type(age))        #datatype
print(type(is_student))

gpa =int(gpa)           #float to int
print(gpa)

name ="Python"          #string to bool
name = bool(name)
print(name)

name = ""
name = bool(name)
print(name)


#input (get output from user)
name = input("What is your name?:")
age = int(input("Type your age:"))

age = age + 1

print(f"Hello {name}!")
print(f"You are {age} years old")
print("Congratulations!")


# Exercise 1
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
print(f"The area is {area} cm^2")




