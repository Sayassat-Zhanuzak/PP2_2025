a = str(input("Enter a word: "))
b = ''.join(reversed(a))
if b == a:
    print(f"{a} is a palindrome!")
else:
    print(f"{a} is NOT a palindrome!")
