import turtle as t
tim = t.Turtle()

def draw_square(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_square(shape_side_n)