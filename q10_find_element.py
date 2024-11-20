'''
Create a program to search for a specific element in a list using a for loop. 
If the element is found, break out of the loop.
'''

dummy_list = ["Hello", 21, 4.53, "keeper"]

to_find = 4.53
for i in range(len(dummy_list)):
    if to_find == dummy_list[i]:
        print(f"Found ({to_find}) at index {i}.")
        break