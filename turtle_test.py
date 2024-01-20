import turtle as t
from random import random

t.shape('turtle')
def basic_move():
    t.right(90)
    t.forward(100)
    t.left(15)
    t.forward(50)
    t.right(120)
    t.forward(100)
    t.done()

def random_steps():
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)
    t.done()

t.speed(1000)
def color_spiral():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(30)
            if steps % 10 == 0:
                t.write(steps)
    t.done()
def crazy_loop():
    angle = 21
    for x in range(1000):
        t.forward(x / 3)
        t.left(x % 20 + 50)
        t.done()

def crazy_loop2():
    angle = 87
    t.speed(5000)
    for x in range(1000):
        t.forward(x)
        t.left(angle)
    t.done()


crazy_loop()