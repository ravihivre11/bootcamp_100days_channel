import ham

hammer = ham.hammer
print(hammer)

bidd ={}
name = input("What is your name? ")
bid = int(input("What is your bid? $"))
bidd[name] = bid

other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

while other == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidd[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
else:
        print("Bidding is closed.")
largest_bid = max(bidd ,key=bidd.get)
print(f"The winner is {largest_bid} with a bid of ${bidd[largest_bid]}")

