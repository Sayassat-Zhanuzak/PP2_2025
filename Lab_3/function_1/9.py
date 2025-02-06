import math
def volume(radius):
    vol = 4*math.pi*(radius**3)/3
    return vol

num = int(input("Radius: "))
result = volume(num)
print(result)