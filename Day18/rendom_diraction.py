import turtle as t 
import random
tim = t.Turtle()

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
directions = [0, 90, 180, 270]


for _ in range (200):
    tim.speed(10)
    tim.color(random.choice(colors))
    tim.forward(100)
    tim.setheading(random.choice(directions))
