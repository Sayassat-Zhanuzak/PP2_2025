import random

random_int = random.randint(1, 20)
print("Hello! What is your name?")
name = input()
trials = 0
print("Well, " + name + ", I am thinking of a number between 1 and 20")
print("Take a guess.")
number = int(input())
while number != random_int:

    if number < random_int and number > 0 and number < 21:
        print("Your guess is too low.")
    elif number > random_int and number > 0 and number < 21:
        print("Your guess is too high.")
    else:
        print("Guess the number between 1 and 20!")
    print("Take a guess")
    number = int(input())
    trials += 1
else:
    print("Good job, " + name + "! You guessed my number in " + str(trials) + " guesses!")
