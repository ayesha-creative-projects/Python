print("Welcome to Temperature Converter!")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C is equal to {round(f, 2)}°F")
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F is equal to {round(c, 2)}°C")
else:
    print("Invalid choice! Please enter 1 or 2.")
