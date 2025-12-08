# Arithmatic
a,b=2,3
c="@"
d="#"
print(a*b*c)
print((a+b)*d)
print((d+c)*b)

n=1
m=2.0
print(n+m)
print(n*m)
print(n/m)
print(n//m)

a=1
b=-2
print(a*b)
print(a/b)
print(b/a)
print(a//b)
print(b//a)

a,b=5,-3
print(a%b)
print(b%a)

print("power : ",2**3)

name=input("Enter name : ")
age=int(input("Enter age : "))
rating=float(input("Enter rating : "))

print(name)
print("my age is : ",age,"and rating is : ",rating,"stars")

# Relational
print(1==2)
print(1!=2)
print(1<=2)

#Assignment
a += b
a = a + b

# Logical
print(True and False)
print(True or False)
print(not False)

# Type Conversion is auto done
a=1
b=3.0
c=a+b
print(c)

#Type Casting is Manually done
a=2
b="4"
c = a + int(b)
print(c)
c= b + str(a)
print(c)


print("THE END",end='')