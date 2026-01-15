import random

# 1
num = random.randint(1, 10) # Python randomly picks a number
print(num)

# 2
dice = random.randint(1, 6)
print("Dice rolled:", dice)

# 3
print("--------------------------")
secret = random.randint(1, 5)
guess = int(input("Guess a number (1-5): "))

if guess == secret:
    print("You win!")
else:
    print("Wrong! Number was", secret)

# 4
secret = random.randint(1, 5)
print("--------------------------")
while True:
    guess = int(input("Guess (1-5): "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try again")


# 5
secret = random.randint(1, 10)

guess = 0
print("--------------------------")
while guess != secret:
    guess = int(input("Guess the number (1-10): "))

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed it.")

print("--------------------------")