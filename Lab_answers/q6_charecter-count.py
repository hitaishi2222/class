'''
Count Specific Character in a String: 
Write a program that counts how many times a specific character appears in a string.
'''

string = "Hello I am cool"
unique_list = set(list(string.replace(" ", "").lower()))

counter = []
res = "The character : Count \n"

for letter in unique_list:
    count = string.lower().count(letter)
    counter.append(count)
    res += f"{letter} : {count}\n"
print(res)