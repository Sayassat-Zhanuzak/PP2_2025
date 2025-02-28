import re

def replace_symbols(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text)
    return result

text = input("Enter your text: ")
new_text = replace_symbols(text)
print("Result: ", new_text)