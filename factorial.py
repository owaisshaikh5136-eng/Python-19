n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    result, i = 1, 1
    while i <= n:
        result *= i
        i += 1
    print(f"{n}! = {result}")
