marks = [10,"nil",25.5]
print(marks)
print(type(marks))

#empty list
empty_list = list()

print(marks[1])
marks[1] = 0
print(marks)

# Slicing
print(marks[:])
print(marks[1:])
print(marks[:1])
print(marks[1:2])

print(marks[-2:-1])

# Add an element at end
marks.append("nil")
print(marks)

marks = [1,4.5,3,10,0,1.0]
# Sort in ascending order
marks.sort()
print(marks)


# Sort in Descending order
marks.sort(reverse=True)
print(marks)

# Reverse
marks = [1,4.5,3,10,0,1.0]
marks.reverse()
print(marks)

# Insert an element at index
marks.insert(3,"new")
print(marks)

# Remove first instant of element
marks.remove(1)
print(marks)

# Delete value at index
marks.pop(2)
print(marks)



print("THE END",end='')