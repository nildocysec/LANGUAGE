# This program find sum of first N natural number and factorial of N

N = int(input("enter a number : "))

sum=0
for i in range(N+1):
    sum += i
print("Sum is : ",sum)

factorial = 1
count=1

while count <= N:
    factorial *= count 
    count += 1
print("Factorial of",N ,"is : ",factorial)

print("THE END",end='')