import os

path = input("Enter the path: ")

if not os.path.exists(path):
    print(f"Path '{path}' does not exist")
else:
    print(f"Path: {path}")
    print("Exists: Yes")
    directory, filename = os.path.split(path)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
