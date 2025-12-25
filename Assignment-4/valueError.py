try:
    a = int(input("Enter a number: "))
    b = a / 2
    print("The result is:", b)
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")

# Output 1:
# Enter a number: 4
# The result is: 2.0

# Output 2:
# Enter a number: a
# Error: Invalid input. Please enter a numeric value.