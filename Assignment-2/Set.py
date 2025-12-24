sampleSet = {1, 2, 3, 4, 5}
# How do you remove all elements from a set in Python?
sampleSet.clear()
print(sampleSet)

# What is the output of the following code snippet?
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)    # Output: {1,2}

# How do you check if an element is present in a set?
element = 3
if element in a:
	print(element, " exists")

# Write a Python program to find the intersection of two sets.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.intersection(set2)
print(set3) # Output: {3,4}

# How does a set handle duplicate values when adding them?
# No errors or exceptions raised and duplicate value not added to set