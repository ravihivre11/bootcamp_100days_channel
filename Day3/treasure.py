# print('''         ____...------------...____
#                _.-"` /o/__ ____ __ __  __ \o\_`"-._
#              .'     / /                    \ \     '.
#              |=====/o/======================\o\=====|
#              |____/_/________..____..________\_\____|
#              /   _/ \_     <_o#\__/#o_>     _/ \_   \
#              \_________\####/_________/
#               |===\!/========================\!/===|
#               |   |=|          .---.         |=|   |
#               |===|o|=========/     \========|o|===|
#               |   | |         \() ()/        | |   |
#               |===|o|======{'-.) A (.-'}=====|o|===|
#               | __/ \__     '-.\uuu/.-'    __/ \__ |
#               |==== .'.'^'.'.====|
#           jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
#               `""""-""""""""""""""""""""""""""-""""` ''')


print("Welcome!! To Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Where do you want to go? Type 'left' or 'right'\n ").lower()
if direction == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    action = input("Type 'wait' for a boat and 'swim' to swim across. \n").lower()
    if action == "wait":
        print("You arrived at the island. There is a house with 3 doors. One red, one yellow and one blue.")
        colour = input("Which colure do you choose? ").lower()
        if colour== "yellow":
            print("You found the treasure! You win!")
        elif colour == "red":
            print("It is a room full of fire. Game over.")
        elif colour == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    elif action == "swim":
        print("You get attacked by an angry crocodile. Game over.")
    else:
        print("You entered wrong value. Game over.")
elif direction == "right":
    print("You fell into a hole. Please enter correct value . Game over.")
else:
    print("You entered wrong value. Game over.")

print("Thank you!!")
