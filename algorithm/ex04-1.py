def sum_n(n):
    if n ==0:
        return 0

    return sum_n(n-1)+n

print (sum_n(10))
print (sum_n(100))
#재귀호출->종료