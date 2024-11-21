'''
Print a Pattern of Stars: Write a program that prints a pattern of stars based on the number of rows input by the user.
'''

user_input = int(input("Enter number of rows of star needed: "))
for stars in range(1,user_input+1):
    print("*"*stars) #✦
    
