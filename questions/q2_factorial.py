'''
Create a program that prompts the user to enter a positive number. 
If the user enters a negative number, use a break statement to exit the loop. 
Otherwise, calculate the factorial of the number using a while loop.
'''

user_input: int = int(input("Enter a positive number to calculate it's factorial: "))
num = user_input

sum = 1
while True:
    if user_input <= 0 :
        break
    else:
        sum *= num
        num -= 1
        if num == 1:
            print(f"Factorial of {user_input} is {sum}.")
            break