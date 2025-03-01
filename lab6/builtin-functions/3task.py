def is_palindrome(s):
    cleaned_s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return cleaned_s == cleaned_s[::-1]  # Check if the reversed string is the same

string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
