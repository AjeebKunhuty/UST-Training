dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# How can you add a new key-value pair to an existing dictionary in Python?
key, value = 'f', 60
dict1[key] = value
print(dict1)

# What happens if you try to access a key that does not exist in a dictionary?
# KeyError raised
try:
    print(dict1['z'])
except KeyError as e:
    print("Error:", e)

# Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
def dictGreaterThan50(d):
    result = [key for key, value in d.items() if value > 50]
    return result

dict1['g'] = 70
print(dictGreaterThan50(dict1))

# How would you iterate over both keys and values of a dictionary in Python?
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

# Write a Python function that merges two dictionaries.
dict2 = {'x': 100, 'y': 200}
dict1.update(dict2)
print(dict1)