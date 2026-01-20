# Random Guess Game using if, else, and elif

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask user to guess
print("Guess a number between 1 and 10")
user_guess = int(input("Enter your guess: "))

# Check the guess using if, elif, else
if user_guess == secret_number:
    print("Correct! You won!")
elif user_guess < secret_number:
    print("Too low! Try again")
    print(f"The correct number was {secret_number}")
else:
    print("Too high! Try again")
    print(f"The correct number was {secret_number}")

print("\n")

# Game 2: Multiple guesses with attempts
print("="*40)
print("Game 2: Guess with 3 attempts")
print("="*40)

secret_number = random.randint(1, 10)
attempts = 3

for i in range(attempts):
    user_guess = int(input(f"Attempt {i+1}: Guess a number between 1 and 10: "))
    
    if user_guess == secret_number:
        print("Correct! You won!")
        break
    elif user_guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if user_guess != secret_number:
    print(f"Game Over! The number was {secret_number}")

print("\n")

# Game 3: Difficulty level selection
print("="*40)
print("Game 3: Choose Difficulty")
print("="*40)

print("Select difficulty:")
print("1 - Easy (1-10)")
print("2 - Medium (1-50)")
print("3 - Hard (1-100)")

difficulty = int(input("Enter 1, 2, or 3: "))

if difficulty == 1:
    max_num = 10
    level_name = "Easy"
elif difficulty == 2:
    max_num = 50
    level_name = "Medium"
elif difficulty == 3:
    max_num = 100
    level_name = "Hard"
else:
    max_num = 10
    level_name = "Easy"

secret_number = random.randint(1, max_num)

print(f"You selected {level_name} mode")
user_guess = int(input(f"Guess a number between 1 and {max_num}: "))

if user_guess == secret_number:
    print("Correct! You won!")
elif user_guess < secret_number:
    print("Too low!")
    print(f"The correct number was {secret_number}")
else:
    print("Too high!")
    print(f"The correct number was {secret_number}")

print("\n")

#  4: Score based on how close you are
print("="*40)
print("Game 4: Closeness Score")
print("="*40)

secret_number = random.randint(1, 100)
user_guess = int(input("Guess a number between 1 and 100: "))

if user_guess == secret_number:
    print("Perfect! Exact match! Score: 100")
elif abs(user_guess - secret_number) <= 5:
    print("Very close! Score: 80")
    print(f"The number was {secret_number}")
elif abs(user_guess - secret_number) <= 10:
    print("Close! Score: 60")
    print(f"The number was {secret_number}")
elif abs(user_guess - secret_number) <= 20:
    print("Not bad! Score: 40")
    print(f"The number was {secret_number}")
else:
    print("Too far! Score: 0")
    print(f"The number was {secret_number}")

print("\n")


