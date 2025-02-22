import re
def match_pattern(text):
    pattern = r'ab*'
    match = re.fullmatch(pattern, text)
    return bool(match)

text = str(input("Enter a word: "))
result = match_pattern(text)
print(result)