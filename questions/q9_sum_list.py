'''
Implement a program to find the sum of all positive numbers in a list using a for loop. 
Skip negative numbers using a continue statement.
'''

num_list = [12,-6,4,-8,3,4,-4,6]
total = 0
for number in num_list:
    if number <= 0:
        continue
    else:
        total += number
print(total)