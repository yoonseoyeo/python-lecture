import turtle as t
n = 36
t.color("yellow")

t.begin_fill()

for x in range(n):
    t.forward (20)
    t.left(360/n)
t.end_fill()