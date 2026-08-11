# Lists:- Containers to store a set of values of any datatype

abc = []
print(abc)

abc = ["Cricket", "Rocket", 234, 64.555, True, False, "0"]

print(abc)

# print(abc[])                        Error!

print(abc[3])

print(abc[2:5])                     # Same slicing as strings

print(abc[1:6:2])

abc[3] = "Ali"                      # Unlike 'strings' 'Lists' are mutable
print(abc[3])
print(abc)