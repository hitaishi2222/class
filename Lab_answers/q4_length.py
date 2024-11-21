'''
Find the Length of a String Without Using len(): 
Write a program to find the length of a string without using Python’s built-in len() function.
'''

word = "Kerala"
length = 0
for letter in word:
    length+=1
print(f"Your word '{word}' has {length} characters.")
