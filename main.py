import sys
class Staff:
    staffCount = 0
    def __init__(self, age, name):  # Constructor
        self.name = name
        self.age = age
        Staff.staffCount += 1
    
    def __str__(self):  # String representation
        if hasattr(self, 'age'):
            return f"Name: {self.name}, Age: {self.age}"
        return f"Name: {self.name} (Age attribute not found)"
    
"""
s1 = Staff(25, "Alice")
print(s1.__str__())
#delattr(s1, 'age')
print(getattr(s1,'name'))
# print(s1.__str__())
# print(s1.__dir__())
# print(dir(s1))
# print(s1.__dict__)
# print(sys.path)
"""

# decorator
def fence(func):
    def add_fence_fn():
        print("*"*10)
        func()
        print("*"*10)
    return add_fence_fn

@fence
def log():
    print("HI")

log()