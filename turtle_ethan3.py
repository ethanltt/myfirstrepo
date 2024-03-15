import turtle as t
def poly(sides,size):
    for x in range(sides):
        t.forward(size)
        t.right(360 / sides)
poly(8,100)
poly(3,250)
t.done()


