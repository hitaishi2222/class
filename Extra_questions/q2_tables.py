'''
Print the multiplication table of a given number using a for loop.
'''

number = int(input("Enter a number which you want a multiplicative table for: "))

for i in range(1,11):
    print(f"{number} x {i} = {number*i}")