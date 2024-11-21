'''
Reverse a number using a while loop
'''

number = 258
res = 0

while number > 0:
    digit = number % 10
    res = res * 10 + digit
    number = number // 10

print(res)