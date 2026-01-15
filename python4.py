# python 4: indexing, while loop, for loop, nested loop

# indexing [start: end: step]
credit_number = "1234-5678-9012-4567"
print(credit_number[:3])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[::3]) #will print evry 3rd character

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] #print backwards
print(credit_number)

# format specifiers = {value:flag} format a value onthe basis of flag inserted
# :10 = allocate spaces
# :< = left justify
# :>= right justify
# :^ = center align
# :+ = use plus sign to indicate positive
# := = place sign to leftmost position
# :  = insert a space 
# :, = comma seperator

price1 = 30005.145673
price2 =-9.5634
price3 = 12.536

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:^10}") # keep in center
print(f"Price 3 is ${price3: }")



# while loop (the condition will run till it bcm true)
# 1
age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

# 2
food = input("Enter a food you like (q for quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q for quit): ")
print("Bye")

# 3
num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10 :
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"You number is {num}")



#for loop (iterate a block of code in fixed number of times)
# 1
for x in range(1,11):
  print(x)
print("HAPPY NEW YEAR!")


# 2
for x in reversed(range(1,11)):
  print(x)
print("HAPPY NEW YEAR!")


# 3
for x in range(1,11,2): # with two gap
  print(x)
print("HAPPY NEW YEAR!")


# 4
credit_card = "1234-5678-90123"
for x in credit_card: 
  print(x)
print("Here your credit card number")


# 5
for x in range(1,21):
  if x == 13:
    continue  # will skip the 13 / break will stop till 12
  else:
    print(x)  # this printing numbers



#nested loop  (outer loop  and then inner loop)
# 1
for x in range(1,10):
   print(x, end=" ") # in one line and add spaces
   

# 2
for x in range(3):
   for x in range(1,10):
      print(x, end="")
   print()


# 3
rows = int(input ("Enter number of rows: "))
columns = int(input ("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
   for y in range(columns):
      print(symbol, end="")
   print()













