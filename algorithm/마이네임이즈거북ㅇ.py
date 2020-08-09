import turtle as t
t.goto(100,50)
t.xcor()
d=t.distance(100,100)
print(d)
ang=t.heading()
ang=t.towards(10,10)
t.setheading(90)
t.home()
def f():
    t.forward(10)
    t.onkeypress(f,"Up")
    t.onscreenclick(t.goto)
    t.title("welcome")
