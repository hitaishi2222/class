'''
Count Words in a String:
Write a program that counts the number of words in a given string.
Assume words are separated by spaces.
'''

string = "Hello, I am cool"
count = len(string.split(" "))
print(f"Given string has {count} words.")
