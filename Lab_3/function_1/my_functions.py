def solve(numheads, numlegs):
    chicken = numlegs/2 - numheads
    rabbit = numheads - chicken
    print("Number of chickens: " + str(chicken))
    print("Number of rabbits " + str(rabbit))

head = int(input("Number of heads: "))
leg = int(input("Number of legs: "))
solve(head, leg)

def histogram(numbers):
    for num in numbers:
        print('*'* num)

sizes = list(map(int, input("Enter numbers: ").split()))
histogram(sizes)

def f_to_c(F):
    print((5/9) * (F - 32))

f_to_c(34)

b = float(input())
f_to_c(b)


def reverse_words(sentence):
    words = sentence.split()
    for word in words[::-1]:
        print(word, end = ' ')

user_input = input("Enter a sentence: ")
reverse_words(user_input)