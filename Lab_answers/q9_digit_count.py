'''
Count the Number of Digits in a String:
Write a program that counts the number of digit characters (0-9) in a given string.
'''

import numpy as np
digits = [str(num) for num in np.arange(10)]

sentence = "My id: 65846085, My score: 89"

repeats = []
res = "Digits : count\n"
for digit in digits:
    counts = sentence.count(digit)
    repeats.append(counts)
    res += f"{digit} : {counts}\n" 
print(res)

# repeats = [sentence.count(digit) for digit in digits]
# res = "Digits : count\n" + "".join([ f"{digit} : {repeat}\n" for digit, repeat in zip(digits, repeats) if repeat!=0 ])
# print(res)



