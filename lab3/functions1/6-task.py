def reverse_words(sentence: str):
    return ' '.join(sentence.split()[::-1])

user_input = input("Enter a sentence: ")
print(reverse_words(user_input))
