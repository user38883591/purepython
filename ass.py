
class Shape:
    def __init__(self,name):
        self.name=name
    def Area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width
    def Area(self):
        print(f"Rectangle:({self.width}*{self.length})")

shape=input("enter name")
width=int(input("enter width"))
length=int(input("enter length"))
print((width*length))

class Triangle(Shape):
    def __init__(self,name,height,base):
        self.myheight=height
        self.mybase=base
    def Area(self):
        print(f"Triangle:({self.myheight}*{self.mybase}")
shape=input("enter name")
height=int(input("enter height"))
base=int(input("enter base"))
print((base*height/2))


