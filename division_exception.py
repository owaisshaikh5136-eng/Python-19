try:
    a = float(input("Numerator: "))
    b = float(input("Denominator: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Enter valid numbers.")
finally:
    print("Finished.")
