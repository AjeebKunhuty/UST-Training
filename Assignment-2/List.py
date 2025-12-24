sampleList = [10, 20, 30, 40, 50]
# How do you add an element at the end of a list in Python?
item = 60
sampleList.append(item)
print(sampleList)

# How can you remove an element from a list by its index?
index = 3
sampleList.pop(index)
print(sampleList)

# What will be the output of the following code snippet?

lst = [1, 2, 3, 4, 5]
lst[1:3] = [10, 20]
print(lst)  # Output: [1,10,20,4,5]


# How can you check if an element exists in a list in Python?
element = 20
if element in sampleList:
	print(element, "exists")
	
# Write a Python function that removes duplicates from a list without using the set() function.
def removeDuplicates(input_list):
    for i in range(len(input_list)-1, 0, -1):
        if input_list[i] in input_list[0:i]:
            del input_list[i]

sample_list = [1, 2, 3, 4, 5, 2,4,41,6,3,1,7,8,5]
removeDuplicates(sample_list)
print(sample_list)