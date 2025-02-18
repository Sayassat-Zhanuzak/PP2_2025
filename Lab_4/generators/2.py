def even_numbers(num):
    for i in range(0, num+1, 2):
        yield i

a = int(input("Enter: "))
for num in even_numbers(a):
    print(num)