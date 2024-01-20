import turtle as t
from random import random

t.forward(100)
t.right(90)
t.forward(100)
t.left(15)
t.forward(50)
# t.right(120)
# t.forward(100)

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.done()