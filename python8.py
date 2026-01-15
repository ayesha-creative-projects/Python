# python 8: file handling, exception

# file handling (means reading from and writing to files.)

# Opening a file
file = open("example.txt", "w")  # Open a file in write mode

# r → read only (default)
# w → write (overwrite file if exists)
# a → append (add at the end)
# r+ → read and write

# writing to a file
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.write("This is a test file.\n")
file.close()  # Always close the file after writing


# reading from a file
file= open("example.txt", "r")
content = file.read()   # Read the whole file
print(content)
file.close()


file = open("example.txt", "r")
for line in file:
    print(line)
file.close()


# Appending to a file
file = open("example.txt", "a")
file.write("Adding a new line.\n")
file.close()


#Using with statement (better way) Automatically closes file for you
with open("example.txt", "w") as file:
    file.write("Hello again!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)



# exception (an error that happens while the program is running.)
#Without handling it, Python stops and shows an error.

# Basic try/except
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong!")

# try: → Python tries to run this code
# except: → If there’s an error, it runs this part instead



#Catch specific errors
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("You did not enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

#ValueError → happens when input is not a number
#ZeroDivisionError → happens when dividing by zero