# python 2: madlibs game, operators, import math and some exercises 

import math
# madlibs game u create a story by random words
noun1 = input("Enter a place or a thing: ")
noun2 = input("Enter a thing or a name: ")
adjective = input("Enter an adjective anything that describes something: ")
verb = input("Enter a word that ends with ed: ")

print(f"Today i went to {noun1},")
print(f"{noun2} was there,")
print(f"the place was so {adjective},")
print(f"i {verb} well with {noun2}.")

#operators and maths
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)  #divide
print(x % y)  #15 % 4 = 3 remainder 3
print(x ** y) #exponent (power) 15 ** 4 = 15 * 15 * 15 * 15 = 50625 
print(x // y) #15 ÷ 4 = 3.75 → floor division = 3

x =3.14
y = 4
z = 5

result = round(x)
result = abs(x)
result = pow(3, 4)
result = max(x, y, z)
result = min(x, y, z)
print(result)

import math 
x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)
print(result)


# Exercise 1
import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)} cm^2")

# Exercise 2
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2)+ pow(b, 2))

print(f"Side c is {c}")

