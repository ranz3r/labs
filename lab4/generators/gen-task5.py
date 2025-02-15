def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = 10
print(list(countdown(n)))
