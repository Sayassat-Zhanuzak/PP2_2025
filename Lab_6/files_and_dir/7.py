source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")

try:
    with open(source, 'r') as src_file:
        contents = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(contents)
    print(f"Contents copied from {source} to {destination}")
except FileNotFoundError:
    print(f"File '{source}' not found")
except Exception as e:
    print(f"An error occurred: {e}")
