def squares(n):
    for i in range(1, n):
        x = i**2
        yield x


x = int(input())
for i in squares(x):
    print(i)

