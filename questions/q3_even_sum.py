'''
Write a Python program to find the sum of all even numbers between 1 and 100 using a while loop. 
Use a continue statement to skip odd numbers.
'''

num: int = 0
sum: int = 0
while num <= 100:
    num += 1
    if num % 2 == 1:
        continue
    sum += num 
print(sum)