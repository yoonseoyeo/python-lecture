import random as r

while True:
    a = r.randint(1,30)
    b = r.randint(1,30)

    print(a, "+", b, "=?")

    x = input()
    c = int(x)

    if a + b == c:
        print("천재!")
    else:
        print("바보?")