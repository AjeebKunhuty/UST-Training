a, b = 10, int(input("Enter a divisor: "))
try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Output 1:
# Enter a divisor: 2
# The result is: 5.0
# 
# Output 2:
# Enter a divisor: 0
# Error: Division by zero is not allowed.