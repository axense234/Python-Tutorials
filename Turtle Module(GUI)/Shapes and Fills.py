import turtle
import random

tim = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# set colors for turtle:
tim.color('red', 'blue')

# set pen width:
tim.width(5)

# fill in shape with color:
tim.begin_fill()
tim.circle(50)
tim.end_fill()

tim.penup()
tim.forward(150)
tim.pendown()

tim.color('yellow', 'black')

# how to type a square:
tim.begin_fill()
for x in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()

for x in range(1000):
    tim.speed(100)
    randColor = random.randrange(0, len(colors))
    tim.color(colors[randColor], colors[random.randrange(0, len(colors))])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    tim.penup()
    tim.setposition((rand1, rand2))
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0, 80))
    tim.end_fill()