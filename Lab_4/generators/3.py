def divisible_3_4(num):
    for i in range(0, num+1):
        if i % 12 == 0: 
            yield i

a = int(input("Enter a number: "))
for i in divisible_3_4(a):
    print(i)