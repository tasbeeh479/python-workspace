# Enter Marks of six students by user and then sort 

Marks = []
print('\t\t->Enter Seven Student Marks<-\n')
f1 = float(input("Enter Student Marks: "))
Marks.append(f1)
f2 = float(input("Enter Student Marks: "))
Marks.append(f2)
f3 = float(input("Enter Student Marks: "))
Marks.append(f3)
f4 = float(input("Enter Student Marks: "))
Marks.append(f4)
f5 = float(input("Enter Student Marks: "))
Marks.append(f5)
f6 = float(input("Enter Student Marks: "))
Marks.append(f6)
print("\nTotal Marks(Before Sort):",Marks)

Marks.sort()
print("\nTotal Marks(After Sort):",Marks)
