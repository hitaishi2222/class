user_input = input("Enter any number: ") 
# print(f"your reversed number is {user_input[::-1]}")

char_length = len(user_input)
reversed_number = ""

for num in range(char_length):
    reversed_number += user_input[char_length-num-1] 

print(reversed_number)
