pi = 3.14159  #global variable, can be used anywhere in the code
def calculate_circumference(radius):
    circumference = 2 * pi * radius  #local variable, only exists inside the function
    return circumference
print(calculate_circumference(6))
enemies = 3  #global variable, exists outside the function and can be used inside the function

def increase_enemies():
    enemies = 4  #local variable, only exists inside the function
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def decrease_enemies():
    global enemies  #tells python to use the global variable instead of creating a local variable
    enemies -= 1
    print(f"enemies inside function: {enemies}")
decrease_enemies()