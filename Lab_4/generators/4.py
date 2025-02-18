def square(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input("First number: "))
b = int(input("Second number: "))
for i in square(a, b):
    print(i)