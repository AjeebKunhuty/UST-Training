try:
    a, b = 10, int(input("Enter a divisor: "))
    print("The result is:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")

# Output 1:
# Enter a divisor: 2
# The result is: 5.0

# Output 2:
# Enter a divisor: 0
# Error: Division by zero is not allowed.

# Output 3:
# Enter a divisor: abc
# Error: Invalid input. Please enter a numeric value.