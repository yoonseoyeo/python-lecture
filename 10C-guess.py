import random as r

n = r.randint(1,5)

while True:
    x = input("맞혀보세요")
    g = int(x)

    if g == n:
        print('정답')
        continue
    if g < n:
        print('너무 작아요')
    if g > n:
        print('너무 커요')