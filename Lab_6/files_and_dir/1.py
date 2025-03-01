import os

path = input("Enter the directory path: ")

if not os.path.exists(path):
    print(f"Path '{path}' does not exist")
else:
    print(f"Path: {path}")
    print("\nDirectories Only")
    dirs = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    print(dirs)

    print("\nFiles Only")
    files = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    print(files)

    print("\nAll Items")
    print(dirs + files)
