nums = {4,9,36,9,"yes",4.0}
print(nums)

null_set = set()
print(null_set)

# Add new element
nums.add("Hi")
print(nums)

# Remove an element
nums.remove(4)
print(nums)

# Remove random element
nums.pop()
print(nums)

# Empty set
nums.clear()
print(nums)

set1 = {1,2,3,4,5,6}
set2 = {2,3,9,8}
# Union
set3 = set1.union(set2)
print(set3)

#Intersection
set4 =set1.intersection(set2)
print(set4)

values = {9,"9"}
print(values)
valuess = {("int" ,9), ("float ",9.0)}
print(valuess)



print("THE END",end='')