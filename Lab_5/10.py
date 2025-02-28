import re

text = input("Enter a text: ")
result = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)
result = result.lower()
print(result)
