import turtle
from random import randrange


def randomStep(turtle, length=10):
    random_num = randrange(0,100)
    if random_num <= 50:
        turtle.left(randrange(180))
    else:
        turtle.right(randrange(180))
    turtle.forward(randrange(length))


def main():
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.color("blue")
    t2 = turtle.Turtle()
    t2.hideturtle()
    t2.color("red")

    myWin = turtle.Screen()

    for i in range(100):
        randomStep(t1)
        randomStep(t2, 20)

    myWin.exitonclick()
main()
