'''
Create a program to find the first even number in a list using a for loop.
Use a break statement to exit the loop as soon as an even number is found.
'''

num_list = [1,5,9,7,6,3,4]

for num in num_list:
    if num % 2 == 0:
        print(f"The first even number in the loop is {num}.")
        break
    