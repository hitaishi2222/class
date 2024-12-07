# list comprehensions
# Generating a list of squares of even numbers between 1 and 20

even_squares = [num*num for num in range(1,21) if num % 2 == 0]

# for num in range(1,21):
#     if num % 2 == 0:
#         print(num * num) 

print(even_squares)

list_strings = ["apple", "ball", "idea", "angle", "arial"]
a_strings = [word for word in list_strings if word.startswith("a")]

# for word in list_strings:
#     if word.startswith("a"):
#         print(word)
print(a_strings)