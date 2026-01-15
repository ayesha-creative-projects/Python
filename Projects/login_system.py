# Step 1: Store usernames and passwords
users = {
    'SPONGBOB': 'spong123#',
    'alia23': '123@alia',
    'Cyber': 'lksw23'
}

# Step 2: Ask for username
while True:  # Keep asking until username is correct
    username = input("Enter your username: ")
    if username in users:
        print("Username found! Now enter your password.")
        break  # Exit the username loop
    else:
        print("WRONG USERNAME! TRY AGAIN")

# Step 3: Ask for password
while True:  # Keep asking until password is correct
    password = input("Enter your password: ")
    if password == users[username]:
        print(f"Login Successful! Welcome, {username}")
        break  # Exit the password loop
    else:
        print("WRONG PASSWORD! TRY AGAIN")
