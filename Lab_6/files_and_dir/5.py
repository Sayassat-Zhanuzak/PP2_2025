path = input("Enter the file path: ")
items = ['apple', 'banana', 'cherry', 'date']

try:
    with open(path, 'w') as file:
        for item in items:
            file.write(item + '\n')
    print(f"List written to file: {path}")
except Exception as e:
    print(f"An error occurred: {e}")
