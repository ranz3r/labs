def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a, b = 2, 6
for num in squares(a, b):
    print(num)
