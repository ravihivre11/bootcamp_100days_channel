import random

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# Generate random number
secret_num = random.randint(1, 100)


difficulty = input("Choose difficulty: easy or hard: ").lower()

# Set attempts
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid input! Please choose 'easy' or 'hard'.")
    exit()

# Game status
won = False

# Main game loop
for i in range(attempts):

    print(f"\nYou have {attempts - i} attempts remaining.")

    guess_number = int(input("Make a guess: "))

    if guess_number > secret_num:
        print("Too high!")

    elif guess_number < secret_num:
        print("Too low!")

    else:
        print(f"You got it! The answer was {secret_num}.")
        won = True
        break

# Lose condition
if not won:
    print(f"\nYou ran out of attempts.")
    print(f"The correct answer was {secret_num}.")

print("\nGame Over.")
print("Thanks for playing!")