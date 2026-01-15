print("Welcome to Weight Converter!")
print("1. Kg to Lbs")
print("2. Lbs to Kg")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    kg = float(input("Enter weight in Kg: "))
    lbs = kg * 2.20462
    print(f"{kg} Kg is equal to {round(lbs, 2)} Lbs")
elif choice == "2":
    lbs = float(input("Enter weight in Lbs: "))
    kg = lbs / 2.20462
    print(f"{lbs} Lbs is equal to {round(kg, 2)} Kg")
else:
    print("Invalid choice! Please enter 1 or 2.")
