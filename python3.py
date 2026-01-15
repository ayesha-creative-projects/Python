"""#python 3: conditions, logical operators, conditional operators, string method

# conditions
age = int(input("Enter ur age: ")) 
# here without int it will give an error bcz input will return
# as string and so the age will so we convert it in int.

if age >= 100:
    print("You r too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age <= 0:
    print("You have'nt born yet")
else:
    print("You must be 18+ to sign up")

name = input("Enter your name? ")
if name=="":
    print("you did'nt enter your name.")
else:
    print(f"Hello {name}")

# logical operators = evalute multiple conditions
# or = at least one condition true
# and = both condition must be true
# not = inverts the condition (T to F and F to T) 

a = 5
b = 10

# True only if both are True
print(a > 0 and b > 5)   # True, because 5>0 AND 10>5
print(a > 0 and b < 5)   # False, because 10<5 is False  

# True if at least one is True
print(a > 0 or b < 5)    # True, because a>0 is True
print(a < 0 or b < 5)    # False, because both are False

print(not a)  # False, reverses True → False
print(not b)  # True, reverses False → True

# 1
temp = 52
is_cloudy = True
if temp > 55 or temp <0 or is_cloudy:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")


# 2
if temp < 55 and is_cloudy:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")"""

# 3
is_raining = True
print(not is_raining)

# 4
has_id_card = False
if not has_id_card:
    print("You cannot enter the exam hall")
else:
    print("You may enter")


# conditional operator (shortcut for if-else)
num = 6
a = 6
b = 7
print("True" if num > 0 else "False")
result = "Even" if num % 2 else "Odd"
max_num = a if a > b else b

print(max_num)

# string method
name = input("Enter full name: ")
phone_number = ("Enter your phone #: ")
result = len(name)
result = name.find("o")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha() #withoutspace = true
result = phone_number.count("-")
phone_number = phone_number.replace("-"," ")

print(result)
print(phone_number)


username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")

else:
    print(f"Welcome {username}")






