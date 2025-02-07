from itertools import permutations

def print_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    print("Permutations:", perms)


string_input = input("Enter a string: ")
print_permutations(string_input)
