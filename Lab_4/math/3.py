import math

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
area = round(n * l**2 * (1/math.tan(math.pi/n)) / 4, 5)
print(area)