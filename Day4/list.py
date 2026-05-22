import random

car = ["BMW", "Mercedes", "Audi", "Toyota", "Honda" , "Ford", "Chevrolet", "Nissan", "Volkswagen", "Hyundai"]
# print(car[2])
# print(car.pop(2)) 

#1
print(random.choices(car))

#2
ran = random.randint(0,9)
print(car[ran])

