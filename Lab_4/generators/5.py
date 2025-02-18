def down(n):
    for i in range(n, -1, -1):
        yield i

a = int(input("Enter: "))
for i in down(a):
    print(i)