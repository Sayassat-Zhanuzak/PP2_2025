class MyString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Введите строку: ")

    def print_string(self):
        print(self.string.upper())

b = MyString()
b.get_string()
b.print_string()
