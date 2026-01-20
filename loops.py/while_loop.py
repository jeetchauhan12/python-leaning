
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
# print(secret_number) # This line is commented out so the game is fun!

# Initialize the number of tries before the loop starts
tries = 0
print("I'm thinking of a number between 1 and 100.")

while True:
    # Get user input and handle potential errors if it's not a number
    try:
        guess = int(input("What's your guess? "))
    except ValueError:
        print("That's not a valid number! Please enter a number.")
        continue # Skip the rest of the loop and ask again

    # Increment the number of tries for each guess
    tries += 1

    if guess == secret_number:
        # Use singular 'try' if tries is 1, otherwise plural 'tries'
        try_str = "try" if tries == 1 else "tries"
        print(f"You got it! The number was {secret_number}.")
        print(f"You guessed it in {tries} {try_str}.")
        break
    elif guess < secret_number:
        print("Too low! Go a little higher.")
    else: # This covers guess > secret_number
        print("Too high! Go a little lower.")