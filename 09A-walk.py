import turtle as t
import random as r

t.shape ("turtle")
t.speed(0)

for x in range(500):
    a= r.randint(1,360) #360 사이 임의의 수 선택해서 a에 입력
    t.setheading(a)   # 거북이 방향을 a 각도로 전환
    t.forward(10)