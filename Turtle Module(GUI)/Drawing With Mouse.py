import turtle
from turtle import Turtle, Screen
import random
import time

screen = Screen()
tim = Turtle('turtle')
tim.speed(-1)
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# what happens when the user tries to drag the turtle
def dragging(x, y):
    tim.ondrag(tim.color(random.choice(colours)))
    tim.setheading(tim.towards(x, y))
    tim.goto(x, y)
    tim.pensize(10)
    tim.ondrag(dragging)

# right click to clear the screen
def clickright(x, y):
    tim.clear()
# the way the turtle acts
def main():
    turtle.listen()
    tim.ondrag(dragging)
    turtle.onscreenclick(clickright, 3)
    screen.mainloop()

main()