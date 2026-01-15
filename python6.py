# python 6: sets, dictionary, index-operator, functions,arguments

#set (no duplicate value)
utencils = {"spoon", "knife", "plates", "fork"}
dishes = {"bowl", "plate", "cup","knife"}

utencils.add("napkin")
dinner_table = utencils.union(dishes)

for x in dinner_table:
    print(x)


# dictionary : allow us to quickly change a value
# 1
capitals = {'USA': 'Washington DC',
          'INDIA': 'New Delhi',
          "France": "Paris",
          'CHINA': 'Beijing'}

print(capitals['INDIA'])
del capitals["USA"]  # removes USA

print(capitals.items())

for key,value in capitals.items():
    print(key,value)

# 2
user = {
    "username": "alia23",
    "password": "123@alia",
    "age": 17
}

print(user["username"])  # alia23
print(user["age"])       # 17

# index operator give access to sequence's elements
name = "Spong bob"

first = name[:6].lower()
last_chr = name[-1]

print(first)
print(last_chr)

# functions
# 1
def hello( ):
    print("HELLO!")
    print("You are in function")

hello()

# 2
def hello(name):
    print("HELLO! " +name)
    print("You are in function")

hello("Bro")

# 3
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


# return statement
def add(number1,number2):
    return number1 + number2

x = add(3,6)
print(x)


# arguments
def hello(first,middle,last):
    print("Hello! " +first+ " " +middle+ " " +last+" " )    

hello(first="Spong",middle="Bob",last="mike")


