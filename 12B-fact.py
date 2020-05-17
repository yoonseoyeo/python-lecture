def fact_func(n):
    fact = 1

    for x in range(1, n+1):
        fact = fact * x

    return fact

print(fact_func(8))
print(fact_func(28))