import turtle as t
t.color("blue")
def snow_line(snow_len):
    if snow_len<=10:
        t.forward((snow_len))
        return
    new_len=snow_len/3
    snow_line(new_len)

    t.left(60)
    snow_line(new_len)
    t.right(120)
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)

t.speed(0)
snow_line(150)
t.right(120)
snow_line(150)
t.right(120)
snow_line(150)
t.hideturtle()
t.done()