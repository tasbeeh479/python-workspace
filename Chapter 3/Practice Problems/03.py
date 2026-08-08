# Q.3 Detect double space in string/text

a = "Once upon a time there was crow"
print(a.find("  "))                         # If double space not present output will be "-1"

b = "Once upon a time  there was crow"
print(b.find("  "))