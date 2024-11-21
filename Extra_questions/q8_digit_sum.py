'''
Find the sum of digits of a number using a while loop.
'''

number = input("Enter a number to find the sum of digits: ")
res = 0
i = 0

while i < len(number):  
    res += int(number[i])
    i+=1
print(res)