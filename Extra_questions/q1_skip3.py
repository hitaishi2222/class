'''
Print all numbers from 1 to 10, but skip multiples of 3 using the continue statement.
'''

for num in range(1,11):
    if num % 3 == 0:
        continue
    print(num)