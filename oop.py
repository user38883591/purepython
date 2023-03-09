class Fruits:
    def __init__(self, type, color, price):
        self.mytype = type
        self.mycolor = color
        self.myprice = price
    def show(self):
        print(self.mytype,"its color is ",self.mycolor,"sold at",self.myprice," each")
myobj=Fruits("Banana","Yellow",20)
myobj.show()
myobj2=Fruits("Oranges","Orange",15)
myobj2.show()

class Employees:
    def __init__(self,name,age,salary):
        self.myname=name
        self.myage=age
        self.mysalary=salary
    def show(self):
        print("my name is",self.myname,"am",str(self.myage),"yrs my salary is",(self.mysalary),)
obj=Employees(" Gathungu Kamau",23,80000)
obj.show()

class Student:
    def __init__(self,name,course,year,stud_regno):
        self.name=name
        self.course=course
        self.year=year
        self.stud_regno=stud_regno
    def show(self):
        print(self.name,self.course,self.year,self.stud_regno)
x=Student("Collins","GEOICT",3,1329)
x.show()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("My name is",self.name ," am " , str(self.age))

class Students(person):
    def __init__(self,name,age,student_id):
        super(). __init__(name,age)
        self.student=student_id
    def show(self):
        super().show()
        print("I am as student with ID"+str(self.student))
name=Students(" Kamau", 23,6789)
name.show()

