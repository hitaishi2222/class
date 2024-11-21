'''
Implement a program to check if a given number is a prime number using a while loop.
if the number has a factor other than 1 and itself, use a break statement to exit the loop.
'''

number: int = int(input("Provide a number to find, it is a prime or not: "))

divisor = 2
while divisor < number:
    if number % divisor == 0:
        print(f"This can be divisible by {divisor}")
        break
    divisor += 1