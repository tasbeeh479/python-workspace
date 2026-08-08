a = "tasbeeh ullah"

print(a.endswith("eh"))        # "TRUE" OR "FALSE"

print(a.endswith("h"))

print(a.startswith("Ta"))      # Error:- Case sensitive

print(a.startswith("ta"))      # "TRUE" OR "FALSE"

print(a.capitalize())          # Only starting letter of 1st word will capitalize (e.g Tasbeeh ullah)

print(a.upper())               # All in 'UPPER CASE'

print(a.lower())               # All in 'LOWER CASE'

# print(a.__str__())            (Only when value od "a" is 'int')

print(a.title())               # CAPITALIZE starting letter of each word

print(a.find("b"))

print(a.isnumeric())

print(a.replace("b","f").replace("tas","ams"))  # Can call multiple times directly in one line

'''
There are many string functions. To simply check you have to just write
"print(a())" and the enter "." after "a", there will be ghost suggestions
or suggestions list of string functions. There you can choose any, what you want
'''