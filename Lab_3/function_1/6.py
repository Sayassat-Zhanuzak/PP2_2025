def reverse_words(sentence):
    words = sentence.split()
    for word in words[::-1]:
        print(word, end = ' ')

user_input = input("Enter a sentence: ")
reverse_words(user_input)