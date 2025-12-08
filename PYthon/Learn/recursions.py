def fun_show(n):
    if(n==0):      #Base Case
        return
    print(n)
    fun_show(n-1)
    print("END")

fun_show(9)

def fun_factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fun_factorial(n-1)

print("factorial is : ",fun_factorial(4))

def fun_natural_num_sum(n):
    if(n==0):
        return 0
    else:
        return n+fun_natural_num_sum(n-1)

print("Sum is :",fun_natural_num_sum(10))


def fun_print_lists(lists,idx=0):
    
    if(idx==len(lists)):
        return
    else:
        print(lists[idx])
        idx+=1
        fun_print_lists(lists,idx)



lists= [1,2,3,"nil"]
fun_print_lists(lists)
