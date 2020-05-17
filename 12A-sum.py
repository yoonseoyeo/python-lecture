## 1부터 n까지의 합을 구하는 함수 정의
def sum_func(n):
    s = 0  # 합을 구하기 위한 변수s(시작 값을 0으로 지정)

    for x in range (1, n +1):  ##range로 1부터 n까지 반복(n+1은 제외)
        s = s +x  ## 지금까지 계산된 값에 x 값을 더해서 s에 저장
    return s  #계산된 s값을 결괏값으로 돌려줌
print(sum_func(10))
print(sum_func(100))
print(sum_func(20000))
