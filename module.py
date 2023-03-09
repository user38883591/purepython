import math
import statistics

import mymodule
mymodule.school(" Emobilis mobile tecnology")
from mymodule import x,y
print(x+y)
from mymodule import w,z
print(w*z)
print(w//z)
print(w/z)
print(w*z)


mymodule.num("")
print(mymodule.x+mymodule.y)
print(mymodule.x-mymodule.y)
print(mymodule.x/mymodule.y)
print(mymodule.x*mymodule.y)
print(mymodule.x//mymodule.y)
print(mymodule.x%mymodule.y)



print(math.sqrt(625))
dataset=[7,12,3,5,19,29,30,57,20]
x=statistics.mean(dataset)
print("mean is",x)
x=statistics.mode(dataset)
print("mode is",x)
x=statistics.variance(dataset)
print("variance is",x)
x=statistics.stdev(dataset)
print("starndard deviation is",x)
x=statistics.quantiles(dataset)
print("quatiles are",x)


# num=[6,9]
# y=statistics.linear_regression(num)
# print("linear regression is",y)

