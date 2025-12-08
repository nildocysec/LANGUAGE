numbers = [1,2,3,4,5,6]
for num in numbers:
    print(num)

x=11
for i in numbers:
    if(i==x):
        print("found",x)
        break
else:
    print("NOT FOUND") # only if loop reached end

# Range(start_from , stop_before , step_size)
for i in range(5,50,5):
    print(i)

for i in range(5):
    print(i)

for i in range(1,10):
    print(i)



print("END OF PROGRAM",end='')