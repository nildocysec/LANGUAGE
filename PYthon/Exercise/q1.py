# This program checks Palindrome for a list

og_list = list()

opt =1
while opt:
    new = input("enter element in list : ")
    og_list.append(new) 
    opt = int(input("Want to enter more element ? 1 for yes 0 for No : "))

copied_list = og_list.copy()
copied_list.reverse()

if(og_list == copied_list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")

print("THE END",end='')