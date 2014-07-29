from turtle import (left, right, forward, speed, hideturtle, exitonclick)

def dragon(level=8, size=200, zig=right, zag=left):
    if level <= 0:
        forward(size)
        return
    size /= 1.41421
    zig(45)
    dragon(level-1, size, right, left)
    zag(90)
    dragon(level-1, size, right, left)
    zig(45)

speed(0)
hideturtle()
dragon(10)
exitonclick()
