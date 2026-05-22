age = int(input("What is your age?"))
price =0
if age < 6 :
    print("the ticket prize is free")
elif age < 18:
    print("the ticket prize is $5")
    price += 5
elif age == 18 or age < 45:
    print("the ticket prize is $10")
    price += 10
elif age >= 45 and age <= 55:
    print("the ticket prize is free")
    price = 0
elif age > 55:
    print("You cant enter the park")
else:
    print("enter right value ")

print(f"your ticket price is ${price}")