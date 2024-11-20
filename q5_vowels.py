'''
Write a program to count the frequency of each vowel in a given string using a for loop.
'''
a_count, e_count, i_count, o_count, u_count, = 0,0,0,0,0

user_input: list[str] = list(input("Enter a word to check the frequency of different vowels: "))
for letter in user_input:
    if letter == 'a':
        a_count += 1
    elif letter == 'e':
        e_count += 1
    elif letter == 'i':
        i_count += 1
    elif letter == 'o':
        o_count += 1
    elif letter == 'u':
        u_count += 1

text = f"Your word has {a_count}->a, {e_count}->e, {i_count}->i, {o_count}->o, and {u_count}->u."
print(text)