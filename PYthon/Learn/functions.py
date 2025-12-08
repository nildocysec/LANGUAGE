# Function Definition
def fun_sum(a,b):
    sum = a+b
    return sum

# Function Calling
sum = fun_sum(3,5)
print(sum)


def fun_product(a=1,b=1): #defualt values at end only
    product = a*b
    return product

print(fun_product())
print(fun_product(2))
print(fun_product(2,3))


def fun_print_list(lists):
    for item in lists:
        print(item,end=' ')

lists= ["aA",1,1.1]
fun_print_list(lists)

def fun_factorial(num):
    fact =1
    for i in range(1,num+1):
        fact = fact*i
    return fact

print(fun_factorial(6))


print("\nSTART is",end=' ')
print("THE END",end='')