def is_palindrom(myword):
    length = len(myword)
    for i in range(length // 2):
        if myword[i] != myword[length - 1 - i]:
            return False
    return True

word = "madam"
word1 = "maam"
print(is_palindrom(word))  # True
print(is_palindrom(word1))  # True
