import re


with open(r'C:\Users\maksa\Desktop\labs\lab5\row.txt', 'r') as f:

    pat = r'(\w)([A-Z]\w+)'
    l = f.read().split()

    for word in l:
        print(re.sub(pat, r'\1 \2', word))
