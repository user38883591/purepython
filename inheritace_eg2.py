class Vehicle:
    def __init__(self, make, model, year):
        self.mymake = make
        self.mymodel = model
        self.myyear = year

    def Enginestart(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")


class Toyota(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year, )
        self.mynum_doors = num_doors

    def Enginestart(self):
        print(f"{self.mymake}{self.mymodel} car with {self.mynum_doors} doors started")


car = Toyota("Hilux", " SUV ", 2020, 4)
car.Enginestart()


class Bike(Vehicle):
    def __init__(self, make, model, year, engine_cap):
        super().__init__(make, model, year)
        self.myengine_cap = engine_cap

    def Enginestart(self):
        print(f"{self.mymake} is a {self.myyear}{self.mymodel} bike with {self.myengine_cap}cc engine")


bike = Bike("Kawasaki Ninja", " sports", 2020, 1200)
bike.Enginestart()
class Lexus(Vehicle):
    def __init__(self,make,model,year,color):
        super(). __init__(make,model,year)
        self.mycolor=color
    def Enginestart(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear}{self.mycolor}")
car=Lexus("LEXUS 570"," Luxurious ",2020," teal")
car.Enginestart()

