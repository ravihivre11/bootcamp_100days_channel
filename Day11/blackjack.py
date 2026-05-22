import random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = random.choices(card, k=2)
print(f"users card is {user_cards}")
print(f"users total is {sum(user_cards)}")


computer_cards = random.choices(card, k=2)
print(f"computer's card is {computer_cards}")
print(f"computer's total is {sum(computer_cards)}")

if sum(user_cards) == 21 and len(user_cards) == 2:
    print("Blackjack! You win!")
elif sum(computer_cards) == 21 and len(computer_cards) == 2:
    print("Computer has Blackjack! You lose!")
elif sum(user_cards) > 21:
    if 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
        if sum(user_cards) > 21:
            print("You lose!")
        else:
            choice = input(f"You want another card? (y/n)")
            while choice == 'y':
                user_cards.append(random.choice(card))
                print(f"users card is {user_cards}")
                print(f"users total is {sum(user_cards)}")
                if sum(user_cards) > 21:
                    print("You lose!")
                else:
                    if sum(user_cards) > sum(computer_cards):
                        print("You win!")
                    elif sum(user_cards) < sum(computer_cards):
                        print("You lose!")
                    else:
                        print("It's a draw!")
            
                if sum(user_cards) > sum(computer_cards):
                    print("You win!")
                elif sum(user_cards) < sum(computer_cards):
                    print("You lose!")
                else:
                    print("It's a draw!")

    else:
        print("You lose!")

elif sum(computer_cards) > 21:
    if 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
        if sum(computer_cards) > 21:
            print("Computer loses!")
        else:
            if sum(user_cards) > sum(computer_cards):
                print("You win!")
            elif sum(user_cards) < sum(computer_cards):
                print("You lose!")
            else:
                print("It's a draw!")
    else:
        print("You lose!")




