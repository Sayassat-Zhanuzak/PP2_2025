import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    try:
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
        print(f"File created: {filename}")
    except Exception as e:
        print(f"An error occurred while creating {filename}: {e}")
