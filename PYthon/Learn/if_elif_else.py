age = int(input("enter your age : "))

if(age>18):
    print("You can vote")

elif(age<18):
    print("You can not vote")

else:
    print("Almost!!😊")


result= "come" if age>18 else "Go"
print(result)

vote = ("yes","no")[age<=18]
print(vote)

salary = float(input("Enter your salary in INR : "))
tax = salary*(0.1,0.2)[salary>1000000]
print("Pay tax of : INR",tax)

num = int(input("Enter a number : "))
if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    print(b)