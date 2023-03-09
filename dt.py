import datetime

x = datetime.datetime.now()
print(x)


def my_func():
    print("my function")
    print("equinox")


my_func()
my_func()
my_func()
my_func()

price = 500
price2 = 600
price3 = 400
text = "price is {} ksh"
print(text.format(price))
print(text.format(price2))
print(text.format(price3))

my_func()


import platform
x= platform.system()
print(x)
x=dir(platform)
print(x)

set={12,24,34,56,78,34}
print("initial set")
print(set)
set.add(13)
set.add(70)
set.add(15)
print("set after adding")
print(set)

class Cars:
    def __init__(self,make,model,classification):
        self.make=make
        self.model=model
        self.classification=classification
    def show(self):
        print(self.make,self.model,self.classification)
myobj=Cars("2016","Toyota","Suv")
myobj.show()
myobj=Cars("2022","Lexus","Luxury")
myobj.show()

class Cladi:
    def __init__(self,type,color,size):
        self.type=type
        self.color=color
        self.size=size
    def show(self):
        print("I flex with my",self.type,"which is",self.color,"in color","of size",self.size)
x=Cladi("Denim","Blue","32")
x.show()
class Machines:
    def __init__(self,type,processor,quality):
        self.type=type
        self.processor=processor
        self.quality=quality
    def show(self):
        print(self.type,self.processor,self.quality)
y=Machines("Hp","corei7","Good")
y.show()

class Clothes:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def show(self):
        print("I love my",str(self.name),"being",str(self.color))

class Cladi(Clothes):
    def __init__(self,name,color,size):
        super(). __init__(name,color)
        self.cladi=size
    def show(self):
        super().show()
        print("I wear size",str(self.Cladi))
    name=Cladi("jeans","red",32)
    name.show()








