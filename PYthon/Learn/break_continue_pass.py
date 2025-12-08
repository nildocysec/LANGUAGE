
for i in range(100):
    pass


i=0
while i<19:
    i+=1
    if(i%2 == 0):
        continue #skip for current iteration
    elif(i%13 == 0):
        break #end loop
    else:
        print(i)


    
