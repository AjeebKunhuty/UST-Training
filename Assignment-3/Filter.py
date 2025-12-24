# Write a Python program using filter() to extract all even numbers from a list.
intList = [5, 2, 9, 1, 6]
evenList = list(filter(lambda x: x%2 == 0, intList))
print(evenList) # Output: [2, 6]

# Write a program using filter() to select all words from a list that start with a vowel.
strList = ["apple", "banana", "cherry", "date", "orange"]
vowelStart = list(filter(lambda s: s[0].lower() in 'aeiou', strList))
print(vowelStart)  # Output: ['apple', 'orange']

# Given a list of integers, use filter() to remove all negative numbers.
intList = [5, 2, 9, 1, 6, -1, -5, -3, -7]
negativesRemoved = list(filter(lambda x: x >= 0, intList))
print(negativesRemoved)  # Output: [5, 2, 9, 1, 6]

# Write a program using filter() to find numbers greater than 50 from a list.
intList = [50, 2, 900, 102, 6, -1, -5, -3, -7, -50, -100, 51]
greater50 = list(filter(lambda x: x > 50, intList))
print(greater50)  # Output: [900, 102, 51]

# Use filter() to extract all palindromic strings from a list.
strList = ["malayalam", "hello", "racecar", "world", "level", "python"]
palindromes = list(filter(lambda s: s == s[::-1], strList))
print(palindromes)  # Output: ['malayalam', 'racecar', 'level']