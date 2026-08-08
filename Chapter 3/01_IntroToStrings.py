# STRING SLICING:-
'''TWO TYPES:-
1: +ive slicing => e.g: name[4], name[3:6]
2: -ive slicing => e.g: name[-7], name[-4:-2]'''

# 1: +ive slicing:-

name = "Tasbeeh"
print(name)
print(len(name))

name1 = name[0]                     # [x] => write index in it (PRINT ONLY THAT LETTER OF COROSSPONDING INDEX)
print(name1)

name2 = name[3]                     # Mean [3:length(last)]
print(name2)

print(name[:3])                     # Mean [0:3]

name3 = name[0:6]                   # Num after ratio does't count MEANS (TO OR UPTO)
print(name3)

name4 = name[3:5] 
print(name4)

print(name[3:])                    # Mean => TOTAL LENGTH [3:7]

# 2: -ive slicing:-                MAP FOR +IVE & -IVE SLICING
                                   # T A S B E E H
print(name[-6])                    # 0 1 2 3 4 5 6
                                   #-7-6-5-4-3-2-1

print(name[-2:-6])                 # NO SYNTAX ERROR BUT LOGICALLY INCORRECT! (can't go reverse)

print(name[-5:])                   # NO ERROR (PRINT -5 WITH LAST LETTER)

print(name[-5:-1])                 # Print -5(S) to -1(H) letter => OUTPUT: SBEE

print(name[-6:-3])                 # Can write corrosponding +ive ratios like: [1:4] 
                                   # To find => SIMPLE TRICK: -ive_ratio - total_letters e.g: here is=> -6+7=1 , -3+7=4

print(name[:-1])

name = "Jake"

print(name)

name[3] = "h"                      # Error(string are immmutable): 'str' object does not support item assignment






