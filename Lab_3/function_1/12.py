def histogram(numbers):
    for num in numbers:
        print('*'* num)

sizes = list(map(int, input("Enter numbers: ").split()))
histogram(sizes)
