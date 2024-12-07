
result = 0

def addition(a,b):
    global result
    num1 = a
    num2 = b
    result += a + b
    print(num1 + num2)
    print(a, b, result)

addition(12, 5)
addition(1, 2)

