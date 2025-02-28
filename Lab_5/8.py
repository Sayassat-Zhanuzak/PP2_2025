import re
text = input("Enter a text: ")
result = re.findall(r'[A-Z][a-z]*', text)
print(result)