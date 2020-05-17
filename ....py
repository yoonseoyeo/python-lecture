import turtle as t
t.color("blue")
def polygon(n):
    for x in range(n):
        t.forward(5)
        t.left(360/n)

def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360 / n)

polygon(36)
#polygon(5)

t.up()
t.forward(50)
t.down()

polygon2(3, 75)
#polygon2(5,100)
