# Write a list comprehension that returns all even numbers from 0 to 20.
evenList = [i for i in range(21) if i % 2 == 0]
print(evenList)

# How would you create a new list of squares from an existing list of numbers using list comprehension?
numList = [1, 2, 3, 4, 5]
squaredList = [ x ** 2 for x in numList]
print(squaredList)

# Write a list comprehension to extract all words that are longer than 4 characters from a sentence.
sentence = "This is a sample sentence for testing"
words = [ word for word in sentence.split() if len(word) > 4]
print(words)

# How can you use list comprehension to generate a list of the first 10 Fibonacci numbers?
fibonacciList = [0,1]
[fibonacciList.append( fibonacciList[-1] + fibonacciList[-2] ) for i in range(2,10)]
print(fibonacciList)

# Can you use an if condition inside a list comprehension? Provide an example where only odd numbers are selected from a list.
oddList = [x for x in numList if x % 2 == 1]
print(oddList)