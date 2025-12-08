str00 = 'first\n@00'
str0 = "second\t@ 2"
str1 = '''one@3'''
str2 = """two@4"""

print(str0,str1)

str12 = str1 + "+" + str2
print(str12)

len_str12= len(str12)
print(len_str12)

# Indexing
str = "my name"
print(str)
print(str[0])
print(str[3])

#str[3] = 'A'  NOT ALLOWED

# Slicing
# str[start_index:end_index]
print(str[1:4])
print(str[:4])
print(str[1:])
print(str[:])

print(str[-5:-1])

# Return true id str end with keyword
print(str.endswith("me"))

# Capitalize first character
print(str.capitalize())
print(str)
str = str.capitalize()
print(str)

# Replace all old value with new value
str = str.replace("m","?")
print(str)

# Find first index of first occurence
print(str.find("na"))
print(str.find("&"))

# Count number of Occurence
print(str.count("n"))


