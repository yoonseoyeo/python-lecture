def sum_n(n):
    f = 1

    for i in range(1,n + 1):
        f = f * i
    return f
print (sum_n(1))
print (sum_n(5))
print (sum_n(10))
