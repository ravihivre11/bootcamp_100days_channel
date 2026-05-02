
rock = ('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

paper = ('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')

scissors = ('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

import random
bot = ["rock", "paper", "scissors"]
print("Welcome to the Rock, Paper, Scissors Game!")
print("What do you choose? type 0 for rock , 1 for paper or 2 for scissors")
bot_choice =random.randint(0,2)

choice = int(input())
if choice == 0:
    print(rock)
    print("Bot choice:")
    print(bot[bot_choice])
    if bot[bot_choice] == "rock":
        print(rock)
        print("It's a draw!")
    elif bot[bot_choice] == "paper":
        print(paper)
        print("You lose!")  
    elif bot[bot_choice] == "scissors":
        print(scissors)
        print("You win!")
    else:
        print("Invalid input! You lose!")



elif choice == 1:
    print(paper)
    print("Bot choice:")
    print(bot[bot_choice])
    if bot[bot_choice] == "rock":
        print(rock)
        print("You win!")
    elif bot[bot_choice] == "paper":
        print(paper)
        print("You lose!")
    elif bot[bot_choice] == "scissors":
        print(scissors)
        print("It's a draw!")
    else:
        print("Invalid input! You lose!")



elif choice == 2:
    print(scissors)
    print("Bot choice:")
    print(bot[bot_choice])
    if bot[bot_choice] == "rock":
        print(rock)
        print("You lose!")
    elif bot[bot_choice] == "paper":
        print(paper)
        print("You win!")
    elif bot[bot_choice] == "scissors":
        print(scissors)
        print("It's a draw!")
    else:
        print("Invalid input! You lose!")



            