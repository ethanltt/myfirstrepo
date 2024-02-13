
import turtle as t

r = range(500)
def poly(size, angle):
    t.setheading(angle)
    r = range(4)
    for x in r:
        t.forward(size)
        t.right(90)


poly(100,180)
poly(50,10)
t.done()