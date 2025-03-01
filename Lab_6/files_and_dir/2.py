import os

path = input("Enter the path: ")

if not os.path.exists(path):
    print(f"Path '{path}' does not exist")
else:
    print(f"Path: {path}")
    print("Exists: Yes")
    print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
    print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
    print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
