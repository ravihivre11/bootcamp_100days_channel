import random
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")
secret_num = random.randint(1,100)
print(secret_num)

difficulty = input("which difficulty do you want to play? type 'easy' or 'hard'")


if difficulty == "easy":
    for i in range(10):
        print(f"You have {10-i} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        
        if guess_number > secret_num:
            print("Too high")
        elif guess_number < secret_num:
            print("Too low")
        elif guess_number == secret_num:
            print(f"You got it! The answer was {secret_num}.")
            break
        else:
            print(f"the correct answer wa {secret_num}.")

elif difficulty == "hard":
    for i in range(5):
        print(f"You have {5-i} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        
        if guess_number > secret_num:
            print("Too high")
        elif guess_number < secret_num:
            print("Too low")
        elif guess_number == secret_num:
            print(f"You got it! The answer was {secret_num}.")
            break
        else:
            print(f"the correct answer wa {secret_num}.")

else:
    print("Invalid input! Please choose 'easy' or 'hard'.")

print("Game Over.")
print("Thanks for playing!")
