
# num = int(input("Enter a number : "))
# i=1
# print("Table of",num,"is : ")
# while i <=10:
#     print(num,"x",i,"=",num*i)
#     i+=1



tups = [1,4,9,16,25]
i=0
while i< len(tups):
    print(tups[i])
    i+=1

i=0
ele = int(input("Enter element to search : "))
while i< len(tups):
    if(tups[i] == ele):
        print(ele,"found at index",i)
    else:
         print("finding...")

    i+=1
    

print("THE END",end='')