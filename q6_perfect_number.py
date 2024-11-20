'''
Write a Python program to print all the perfect numbers between a given range.
'''

user_input = int(input("Display perfect numbers below: "))

factors = []

for i in range(1, user_input+1):
    for n in range(1, i+1):
        if i % n == 0:
            factors.append(n)
    if sum(factors)-i == i:
        print(i)
    # print(f"sum = {sum(factors)-i} -> {i}")
    factors = []

