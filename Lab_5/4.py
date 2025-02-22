import re
text = str(input("Enter: "))

def find_matches(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

for x in find_matches(text):
    print(x)

