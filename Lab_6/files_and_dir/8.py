import os

path = input("Enter the file path to delete: ")

if not os.path.exists(path):
    print(f"Path '{path}' does not exist")
elif not os.access(path, os.W_OK):
    print(f"Access denied: Cannot delete '{path}'")
else:
    try:
        os.remove(path)
        print(f"File '{path}' has been deleted")
    except Exception as e:
        print(f"An error occurred: {e}")
