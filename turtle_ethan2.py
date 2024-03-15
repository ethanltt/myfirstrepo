
import turtle as t


def poly(size, angle, speed, color):
    t.color(color)
    r = range(4)
    t.setheading(angle)
    t.speed(speed)
    for x in r:
        t.forward(size)
        t.right(120)

for x in range(1000):
    poly(2*x,130*x, 200,"blue")
