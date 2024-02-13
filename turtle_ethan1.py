import turtle as t
def pooooo():
    t.speed(1000)
    for x in range(1000):
        print(x % 10)
        t.forward(200)
        t.right(70)
        t.forward(100)
        t.right(70)
        t.forward(200 + x)
        t.right(90)
        t.forward(100)
    t.done()

def triangle(s):
    t.speed(100)
    t.setheading(s)
    t.forward(s)
    t.right(120)

    t.forward(s)
    t.right(120)

    t.forward(s)
    t.right(120)




r = range(500)
for x in r:
    triangle(x*3)
t.done()