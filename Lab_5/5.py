import re
def find_matches(text):
    pattern = r'a.*b'
    matches = re.findall(pattern, text)
    return matches

text = str(input("Enter: "))
result = find_matches(text)

for x in result:
    print(x)