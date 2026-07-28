try:
    age = int(input("What is your age? "))

except ValueError:
    print("Please enter a valid number.")

if age < 18:
    print("You are not old enough to drive.")