# Creating Class
class student:
    std1 = ["Nil",22,4.5]
    std = 12

# Instance of class / object creation
s1 = student()
print(s1.std)
print(s1.std1)

class cars:

    # Defualt constuctor no need of creating
    #def __init__(self):
    #    print("Hello ji..")

    showroom_name = "NIL AUTOMOBILES AND MOTORS"
    
    # Constructor
    def __init__(self, brand , price):     # self point on same class which object created
        print("Welcome to car showroom",self.showroom_name)
        
        self.brand = brand

        self.prices = price

car1 = cars("bmw",10)
print(car1.brand)

car2 = cars("tesla",100)
print(car2.brand)

car3 = cars("tata", 1000)
print("price is: ",car3.prices)


class students():

    # Static method
    @staticmethod # Decorator
    def print_hello():
        print("hello hi")

    def __init__(self, name, marks):
        self.name = name
        print("Welcome",self.name)
        self.marks = marks
        
      #Method    
    def fun_average_marks(self):
        sum = 0
        for mark in self.marks:
            sum += mark

        average = sum/3
        print("your Average score is : ",average)

s1 = students("Nil",[6,7,11])
s1.fun_average_marks()
s1.name = "newname"
print(s1.name)
s1.print_hello()

class account():

    def __init__(self, id, password, balance):
        print("Welcome to World bank")
        self.id = id

        self.__password = password # adding two underscore make it private outside class
        print(self.__password) # accesible in class
        self.__its_private()

        self.balance = balance

    def print_balance(self):
        print("your balance is : INR",self.balance)

    def debit(self,amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        print("Amount Deducted")
        self.print_balance()

    def credit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Amount Added")
        self.print_balance()

    def __its_private(self):
        print("its private method")

c1 = account(101,"mypass",10000)
c1.print_balance()
c1.debit(5000)
c1.credit(99)
#print(c1.__password)
#c1.__its_private()


# Delete object or its properties
del c1

# Inheritance
class car():        #parent class
    
    name  = "i AM"
    # Class method
    @classmethod        # to change or access class attributes
    def change_name(cls, name):
        cls.name = name
        #car.name = name
        #self.__class__.name = name

    @staticmethod
    def car_start():
        print("car started")
    
    @staticmethod
    def car_stop():
        print("car stopped")

class bike():
    print("welcome to bike show room")

class tata(car):    # child class
    def __init__(self,model):
        self.model = model

class creta(tata):
    def __init__(self, car_type):
        self.type = car_type
        super().car_start()     # use super() to acess methods of parent class

class vehicle(car, bike):
    def __init__(self):
        print("welcome to new vehicles")


c1 = tata("nano")
c2 = tata("creta")
c1.car_start()
c2.car_stop()

c3 = creta("electric")

c4 = vehicle()

c5 = car()
c5.change_name("nilkill")
print(c5.name)
print(car.name)

class std():
    def __init__(self,p ,c ,m ):
        self.p = p
        self.c = c
        self.m = m

    @property       #return value updates if any attributes value changes
    def average(self):
        return (self.p+self.c+self.m)/3 

s1 = std(99, 95, 91)
print(s1.average)
s1.p = 90
print(s1.average)


# PolyMorphism
print(1+3)
print("my"+"name")
print([1,2,3] + [2,3,4])


''' Dunder Functions
      a__add__b         = a+b
      a__sub__b         = a-b
      a__mul__b         = a*b
      a__truediv__b     = a/b
      a__mod__b         = a%b
'''

class complex():
      
      def __init__(self,real,img):
            self.real = real
            self.img = img
      
      def print_complex(self):
            print(self.real,"i +",self.img,"j")

      def __add__(self,num2):
            new_real = self.real + num2.real
            new_img = self.img + num2.img
            print(new_real,"i +",new_img,"j")


num1 = complex(1,3)
num1.print_complex()

num2 = complex(4,5)
num2.print_complex()

num3 = num1 + num2

class circle():
      def __init__(self,radius):
            self.radius = radius

      def circle_area(self):
            area = (self.radius)*(self.radius)*(3.14)
            print("Area is : ",area)

c1 = circle(7)
c1.circle_area()

class order():
      def __init__(self,item,price):
            self.item = item
            self.price = price
      
      def __gt__(self, item2):
            if(self.price > item2.price):
                  return True
            else:
                  return False

o1 = order("tea",100)
o2 = order("coffee",200)
print(o2 > o1)

