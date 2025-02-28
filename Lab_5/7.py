import re
text = input("Enter a text: ")

pattern = r'_([a-z])'
result = re.sub(pattern, lambda x: x.group(1).upper(), text)

print("CamelCase: ", result)