# 0 1 1 2 3 5 8 13

a = 0
b = 1
c = 0

print(a, b)
for n in range(20):
    c = a + b
    print(c)
    a = b
    b = c