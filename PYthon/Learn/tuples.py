tup = (1,2,"nil",3.0,2.0)
print(tup)
print(tup[1])
print(type(tup))

# tup[1] = 4 #NOT ALLLOWED

tup_solo = (1,)
print(tup_solo)

# Slicing
print(tup[:])

# Find index of first instance of element
print(tup.index("nil"))

# Frequency of element
print(tup.count(2))

movie1 = input("Enter favourite movie : ")
movie2 = input("Enter favourite movie : ")
movie3 = input("Enter favourite movie : ")
favourite_movies = [movie1,movie2,movie3]
print("favourite movies are : ",favourite_movies)

# This program checks Palindrome
og_list = [1,2,3,2,1.0]
copied_list = og_list.copy()
copied_list.reverse()

if(og_list == copied_list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")

print("THE END",end='')
