'''
Print a Diamond Pattern of Stars: 
Write a program that prints a diamond pattern of stars based on the number of rows input by the user.
'''


rows = int(input("Enter the diamond row height: "))

for row in range(0,2*rows+1):
    if row > rows :
        row = 2*rows - row
    print(f"{' '*(rows-row)}{'*'*((2*row+1))}{' '*(rows-row)}")

