'''
Tuples are IMMUTABLE cannot change. You can use it in calculation,
functions etc. For storing its ANSWER you should make another TUPLE.
You cannot store it in existing TUPLE
'''

a = (23,34.5,"tasbeeh",True,"Rohan",2343423.234,True)
print(a)

print(a.count(True))            # How many times it came in data?
#OR
# a = a.count(True)
# print(a)

print(a.index(True))            # Only check 1st one and return

b = (23,"qwerty","ABCD",234.55)

result = a + b
print(result)

Repeat = a * 2                  # Can repeat tuple
print(Repeat)                           

print("Rohan" in a)             # Checking Membership