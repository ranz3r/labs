def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = 50
print(list(divisible_by_3_and_4(n)))
