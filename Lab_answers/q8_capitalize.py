'''
Capitalize the First Letter of Each Word:
Write a program that capitalizes the first letter of each word in a given string.
'''

string = "Python is a wonderful language."
updated = [word.capitalize() for word in string.split(" ")]

print(" ".join(updated))
# print(*updated, sep= " ")