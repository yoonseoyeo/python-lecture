import turtle as t

t.bgcolor('yellow')
t.speed(0)

for x in range(200):
    if x %3 == 0:
        t.color('blue')
    if x %3 == 1:
        t.color('purple')
    if x %3 == 2:
        t.color('red')
    t.forward(x * 2)
    t.left(100)
input('aa')