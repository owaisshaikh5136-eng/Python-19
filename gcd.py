def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
x = int(input("First integer: "))
y = int(input("Second integer: "))
print("GCD =", gcd(x, y))
