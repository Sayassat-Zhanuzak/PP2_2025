"""
a - rabbit number
b - chicken number
a + b = 35
4a + 2b = 94 -> 2a + b = 47

b = 35 - a
2a + 35 - a = 47 

a (chicken) = 47 - 35 = 12 divide numlegs by two then substract numheads
b (rabbit) = 35 - 12 = 23 substract a from numheads
"""

def solve(numheads, numlegs):
    chicken = numlegs/2 - numheads
    rabbit = numheads - chicken
    print("Number of chickens: " + str(chicken))
    print("Number of rabbits " + str(rabbit))

solve(35, 94)