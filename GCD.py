def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

ans = gcd(a:=15, b:=30)

print(f"GCD of {a} and {b} is : {ans}")

