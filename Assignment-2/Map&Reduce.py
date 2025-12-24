# How does the map() function work in Python? Give an example where you square each number in a list.
# Syntax: map(function, iterable) # applies function to each value in iterable
squaredNums = map( lambda x : x**2, [1,2,3,4])
print(list(squaredNums))	# Output: [1,4,9,16]

# What is the output of the following code?

from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)   # Output: 24

# How would you use the map() function to convert all string elements of a list to uppercase?
stringList = ['Hello', 'world', 'from', 'Python']
print(list(map(lambda s: s.upper(), stringList)))

# Write a Python program that uses reduce() to find the greatest common divisor (GCD) of a list of numbers.
from math import gcd
numList = [12, 18, 24, 30]
print(reduce(gcd,numList))

# Compare and contrast the map() and filter() functions in Python.
# Map function subjects every element in iterable to the given argument function and appends return value to the result.
# Filter function subjects every element in iterable to the given argument function and appends the currently pointed iterable value to the result if only the function returned True.