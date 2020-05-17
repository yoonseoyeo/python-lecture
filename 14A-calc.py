import random as r

def make_question():

    a = r.randint(1,40)
    b = r.randint(1,20)
    op = r.randint(1,3)

    q = str(a)

    if op == 1:
        q = q + "+"
    elif op == 2:
        q = q + "-"
    elif op == 3:
        q = q + "*"


    q = q+ str(b)

    return q

sc1 = 0
sc2 = 0

run = True

step = 0
while run:
    step = step +1
    print ("Step",step)

    for x in range(5):
        q = make_question()
        print(q)
        ans = input("=")


        if ans == 'quit':
            run = False
            break
        if ans == "" or ans == "":
            continue

        ret = int(ans)
        if eval(q) == ret:
            print("정답!")
            sc1 = sc1 + 1
        else:
            print("오답!")
            sc2 = sc2 + 1

    print("정답:", sc1, "오답:", sc2)
    if sc2 == 0:
        print("당신은 천재입니다!")
