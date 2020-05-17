import turtle as t
import time
n = 1000

t.bgcolor('green')

t.color('yellow')

t.speed(0)

for x in range(n):
    t.circle(80)
    t.left(360/n)

time.sleep(5)