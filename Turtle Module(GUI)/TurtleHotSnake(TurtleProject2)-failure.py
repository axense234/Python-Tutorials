import turtle
import time
import random
import sys

WIDTH, HEIGHT = 1000, 600
COLOURS = ['green', 'blue', 'yellow', 'pink', 'black', 'orange', 'purple', 'red', 'brown', 'cyan']
timelimit = ''

def createscreen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Hot Snake')


def gamestartdraw():
    GameStart = turtle.Turtle()
    # Letter G
    GameStart.color('black')
    GameStart.shape('turtle')
    GameStart.speed(-1)
    GameStart.width(8)
    GameStart.hideturtle()
    GameStart.penup()
    GameStart.goto(-400, 0)
    GameStart.pendown()
    GameStart.left(90)
    GameStart.forward(80)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.backward(30)
    GameStart.left(90)
    GameStart.backward(80)
    GameStart.right(90)
    GameStart.forward(50)
    GameStart.left(90)
    GameStart.forward(30)
    GameStart.left(90)
    GameStart.forward(20)
    # Letter A
    GameStart.penup()
    GameStart.goto(-340, 0)
    GameStart.pendown()
    GameStart.right(115)
    GameStart.forward(94.3)
    GameStart.right(128)
    GameStart.forward(94.3)
    GameStart.backward(47)
    GameStart.left(245)
    GameStart.forward(40)
    # Letter M
    GameStart.penup()
    GameStart.goto(-240, 0)
    GameStart.right(90)
    GameStart.pendown()
    GameStart.forward(80)
    GameStart.right(145)
    GameStart.forward(80)
    GameStart.left(105)
    GameStart.forward(80)
    GameStart.right(140)
    GameStart.forward(80)
    # Letter E
    GameStart.penup()
    GameStart.goto(-100, 0)
    GameStart.pendown()
    GameStart.left(180)
    GameStart.forward(80)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.backward(30)
    GameStart.left(90)
    GameStart.backward(40)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.backward(30)
    GameStart.left(90)
    GameStart.backward(40)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.hideturtle()
    # Letter S
    GameStart.penup()
    GameStart.goto(50, 0)
    GameStart.pendown()
    GameStart.forward(40)
    GameStart.left(90)
    GameStart.forward(40)
    GameStart.left(90)
    GameStart.forward(40)
    GameStart.right(90)
    GameStart.forward(40)
    GameStart.right(90)
    GameStart.forward(40)
    # Letter T
    GameStart.penup()
    GameStart.goto(150, 0)
    GameStart.pendown()
    GameStart.left(90)
    GameStart.forward(80)
    GameStart.left(90)
    GameStart.forward(30)
    GameStart.backward(60)
    # Letter A
    GameStart.penup()
    GameStart.goto(170, 0)
    GameStart.pendown()
    GameStart.right(115)
    GameStart.forward(94.3)
    GameStart.right(135)
    GameStart.forward(94.3)
    GameStart.backward(47)
    GameStart.left(245)
    GameStart.forward(40)
    # Letter R
    GameStart.penup()
    GameStart.goto(275, 0)
    GameStart.right(85)
    GameStart.pendown()
    GameStart.forward(80)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.right(90)
    GameStart.forward(30)
    GameStart.right(180)
    GameStart.right(50)
    GameStart.forward(60)
    GameStart.left(50)
    # Letter T
    GameStart.penup()
    GameStart.goto(360, 0)
    GameStart.pendown()
    GameStart.left(90)
    GameStart.forward(80)
    GameStart.left(90)
    GameStart.forward(30)
    GameStart.backward(60)


# Start of the game
createscreen()
gamestartdraw()
time.sleep(2)
turtle.clearscreen()
time.sleep(1)
# Beggining of the game

snake = turtle.Turtle()
snake.color('green', 'darkgreen')
snake.shape('square')
snake.width(7)

def up():
    snake.setheading(90)
    snake.forward(10)


def down():
    snake.setheading(270)
    snake.forward(10)


def left():
    snake.setheading(180)
    snake.forward(10)


def right():
    snake.setheading(0)
    snake.forward(10)


def turtlecontrol():
    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')

turtlecontrol()
water = turtle.Turtle()
water.hideturtle()
water.color('black', 'aqua')
water.speed(-1)
water.width(5)
water.penup()
rand1 = random.randrange(-300, 280)
rand2 = random.randrange(-300, 280)
water.setposition((rand1, rand2))
water.pendown()
water.begin_fill()
water.circle(25)
water.end_fill()

def modifyscreen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    s = 30
    while s >= 1:
        screen.title('Hot Snake!!!' + '\n' + 'Time Limit: ' + str(s))
        time.sleep(1)
        s -= 1
        turtlecontrol()
        if s == 0:
            print("Game Over!")
            sys.exit()

modifyscreen()
turtle.mainloop()