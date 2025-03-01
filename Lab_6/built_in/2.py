a = str(input("Enter a word: "))
cnt_upper = 0
cnt_lower = 0
for i in a:
    if i.isupper():
        cnt_upper += 1
    if i.islower():
        cnt_lower += 1

print("Number of uppercase letters: ", cnt_upper)
print("Number of lowercase letters: ", cnt_lower)