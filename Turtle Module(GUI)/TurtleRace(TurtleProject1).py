import turtle
import random
import time

WIDTH, HEIGHT = 1000, 700
COLOURS = ['green', 'blue', 'yellow', 'pink', 'black', 'orange', 'purple', 'red', 'brown', 'cyan']
def getting_the_number_of_turtles():
    while True:
        racers = input("Chose an amount of turtles that will race!(2 - 10) ")
        if racers.isdigit():
            racers = int(racers)
        elif not racers.isdigit():
            print("That's not a number,please input one! Try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number of racers not between 2 and 10!")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]



def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        turtles.append(racer)
        racer.pendown()
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing 2000')

racers = getting_the_number_of_turtles()
init_turtle()
random.shuffle(COLOURS)
colors = COLOURS[:racers]

winner = race(colors)
print('The winner is the turtle with color:' + winner + '!')
time.sleep(5)