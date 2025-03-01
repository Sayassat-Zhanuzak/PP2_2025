import time
import math
num = float(input("Enter a number: "))
mili = int(input("Enter a time (miliseconds): "))

time.sleep(mili/1000)
square_root = num**0.5

print(f"Square root of {num} after {mili} miliseconds is {square_root}.")