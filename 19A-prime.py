x = int(input("? "))
d = 2

while d <= x:
    if x % d == 0:
        print(d)
    else:
        x = x/d
        d = d+1