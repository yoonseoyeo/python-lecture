import turtle as t
t.color("blue")
def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360 / n)

#polygon(3)
#polygon(5)

#t.up()
#t.forward(100)
#t.down(),

polygon2(30,31)
#polygon2(5,100)
