import re


with open(r'C:\Users\maksa\Desktop\labs\lab5\row.txt', 'r') as f:

    pat = r'ab*'
    l = f.read().split()
    for word in l:
        if re.fullmatch(pat, word):
            print(word)