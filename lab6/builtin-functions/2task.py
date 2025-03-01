def count_case_letters(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    return upper_case, lower_case

string = input("Enter a string: ")
upper, lower = count_case_letters(string)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
