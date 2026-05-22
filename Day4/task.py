import random 
import my_random

print(my_random.my_fav)

print(random.randint(1,10))
print(random.random())
print(random.uniform(1,2))

list = ["BMW", "VOLVO","MUSTANG", "AUDI" ,"RR", "MERCEDES","PORSCHE", "FERRARI", "LAMBORGHINI", "JAGUAR"]
print(random.choice(list))
print(random.choices(list ,k=2))  #k is the no. of items u have to display
print(random.sample(list, k=2))  #k is the no. of items u have to display but it will not repeat the same item




print(random.shuffle(list))