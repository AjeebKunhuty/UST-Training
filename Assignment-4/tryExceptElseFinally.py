try:
    a = 10
    b = int(input("Enter a divisor: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division successful.")
finally:
    print("Execution completed.")

# Output 1:
# Enter a divisor: 0
# Error: Division by zero is not allowed.
# Execution completed.

# Output 2:
# Enter a divisor: 2
# Result: 5.0
# Division successful.
# Execution completed.