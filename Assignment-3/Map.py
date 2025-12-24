# Write a Python program using map() to convert a list of integers into their squares.
intList = [5, 2, 9, 1, 6]
squaredList = list(map(lambda x: x**2, intList))
print(squaredList)  # Output: [25, 4, 81, 1, 36]

# Write a program using map() to convert all strings in a list to uppercase.
strList = ["apple", "banana", "cherry", "date"]
upperStrList = list(map(lambda s: s.upper(), strList))
print(upperStrList)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE']

# Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
celsiusList = [0, 10, 20.5, 30, 40.2, 50]
fahrenheitList = list(map(lambda c: (c * 9/5) + 32, celsiusList))
print(fahrenheitList)  # Output: [32.0, 50.0, 68.9, 86.0, 104.36, 122.0]

# Write a program using map() to calculate the length of each word in a list of strings.
strList = ["apple", "banana", "cherry", "date"]
lenStrList = list(map(lambda s: len(s), strList))
print(lenStrList)  # Output: [5, 6, 6, 4]

# Use map() to add 10 to each element of a given list of numbers.
intList = [5, 2, 9, 1, 6]
tenList = list(map(lambda x: x+10, intList))
print(tenList)  # Output: [15, 12, 19, 11, 16]