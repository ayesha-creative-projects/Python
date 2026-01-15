# python compound interest calculator

principle = 0
rate = 0
time = 0

while True: #instead write principle <= 0 use True for both 0 and any number for user to enter
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("interest rate can't be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time in year: "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

