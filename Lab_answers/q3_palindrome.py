'''
Check for Palindrome:
Write a program to check if a given string is a palindrome (a string that reads the same backward as forward)
'''

user_input: str = input("Give a word to reverse: ")
if user_input.lower() == user_input[::-1].lower():
    print(f"The word '{user_input}' is a palindrome.")
else:
    print(f"The word '{user_input}' is not a palindrome.")
