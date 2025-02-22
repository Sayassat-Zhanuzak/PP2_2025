import re

def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, text)
    yield matches

text = input("Enter a sentence: ")  
result = find_sequences(text)

for x in result:
    print(x)