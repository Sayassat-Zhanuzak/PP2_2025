import re
def match_pattern(text):
    pattern = r"ab{2,3}"
    match = re.findall(pattern, text)
    return match

text = str(input("Enter a word: "))
result = match_pattern(text)
print(result)


