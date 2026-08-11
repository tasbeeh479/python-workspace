# Lists are MUTABLE. We can the existing list easily

abc = ["Cricket", "Rocket", 234, 64.555, True, False, "0"]
abc.append("Amjad")
# print(abc.sort())           #Error: not supported between instances of 'int' and 'str'
print(abc)

b = [23,"qwerty","ABCD",234.55]

result = abc + b
print(result)

# print(abc.clear())

asd = [2345,46.4,3.4,4356,6578,0,456,345.45645656]
print(asd.sort())           # For same data types (Mostly for numbers) e.g (ent,float etc) => Prints "None" as output.

print(asd)

print(abc.copy())           # Return shallow copy of the list

# print(abc.clear())          # Clear whole list  OUTPUT:None
# print(abc)

print(abc.reverse())
print(abc)

print(abc.remove("Amjad"))     # Writing "print" with function will print its 'return' value (showing what is done here)
print(abc)

print(abc.pop(3))               # Delete + Print or return or show what is done here. e.g OUTPUT: prints value at index '3' 
print(abc)

# abc.pop(3)                    Function will Just do its work ==> "DELETE". e.g Will not show its work, what is done...

abc.insert(3,"Tasbeeh")         # insert "Tasbeeh" at index '3'. Also here it will do its work not showing what is done.
print(abc)

abc = abc.count(True)           # How many times it came in data?
print(abc)