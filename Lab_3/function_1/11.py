word = str(input("type a word: "))
# char_list = list(word)
char_list = [char for char in word]
reversed_char_list = list(reversed(char_list))
if char_list == reversed_char_list:
    print("YES")
else:
    print("NO")

#the second option
if word == word[::-1]:
    print("YES")
else:
    print("NO")