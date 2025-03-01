path = input("Enter the file path: ")

try:
    with open(path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print(f"File '{path}' not found")
except Exception as e:
    print(f"An error occurred: {e}")
