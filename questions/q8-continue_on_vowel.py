'''
Write a Python program to iterate over a string using a for loop.
If the character is a vowel, use a continue statement to skip it.
'''

word: str = "Cyclopes"
vowels = 'aeiou'
for letter in word:
    if letter.lower() in vowels:
        continue
    else:
        print(letter)