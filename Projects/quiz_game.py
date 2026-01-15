# Python quiz game

print("---------------------------------------------")
print("|            WELCOME TO QUIZ WORLD          |")
print("---------------------------------------------")
questions = ("1. How many bones are in human body?: ",
             "2. Which planet is known as the Red Planet?: ",
             "3. Which ocean is the largest in the world?: ",
             "4. What is the opposite of “hot”?: ",
             "5. What gets wetter the more it dries?: ",)

options = (("A. 309", "B. 224", "C. 206", "D. 119"),
           ("A. Mercur", "B. Saturn", "C. Jupiter", "D. Mars"),
           ("A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean"),
           ("A. Ice", "B. Cold", "C. Fire", "D. Rain"),
           ("A. Towel", "B. Sponge", "C. Water Bottle", "D. Soap"),)

answers = ("C", "D", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1   

print("------------------------") 
print("        RESULTS         ") 
print("------------------------") 

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions)* 100) # len questions means # of total questions
print(f"Your score is: {score}%")





