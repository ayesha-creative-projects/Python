import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60 
    minutes = int(x / 60) % 60 
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP!")

#seconds = x % 60
#  Gives the leftover seconds after counting full minutes
#  Example: 125 seconds → 125 % 60 = 5 → 5 seconds
#minutes = int(x / 60) % 60
#  Converts total seconds to minutes, then % 60 keeps it < 60
#  Example: 125 seconds → 125 / 60 = 2 → 2 minutes
#hours = int(x / 3600)
#  Converts total seconds to hours
#  Example: 4000 seconds → 4000 / 3600 = 1 hour