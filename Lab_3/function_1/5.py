from itertools import permutations

def string_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms

input_string = "abc"
result = string_permutations(input_string)
print("All permutations of the string:", result)
