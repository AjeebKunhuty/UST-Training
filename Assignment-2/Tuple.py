# Can you modify the elements of a tuple after it has been created? Why or why not?
# No, because tuples are immutable. 
# Workaround to this problem is to convert tuple to list, change value and convert it back to a tuple.

sampleTuple = (1, 2, 3, 4, 5)
# How would you access the second-to-last element in a tuple?
print(sampleTuple[-2])

# What is the difference between a list and a tuple in Python?
# List is mutable and Tuple is immutable
try:
    sampleTuple[2] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
t = (1, 2, 3, 4)
tupleAsList = list(t)
tupleAsList[2] = 100
t = tuple(tupleAsList)
print(t)

# Write a Python function that takes a tuple of numbers and returns the sum of all its elements.
def tupleSum(tup):
	return sum(tup)

print(tupleSum(t))
