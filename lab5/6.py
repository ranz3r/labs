import re


with open(r'C:\Users\maksa\Desktop\labs\lab5\row.txt', 'r') as f:

    pat = r'[ ,.]'
    l = f.read().split()

    for word in l:
        print(re.sub(pat, ':', word))