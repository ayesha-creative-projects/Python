import random
print("Welcome to Password generator")

letters = ["a", "b", "c", "d", "A", "B", "C"]
numbers = ["1","2","3","4"]
symbols = ["!","@","#","$"]

length = int(input("Enter password length: "))
password = ""

for i in range(length):
    password += random.choice(letters + numbers + symbols)

print("Your password is:", password)



