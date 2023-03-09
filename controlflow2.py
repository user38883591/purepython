marks=int(input("my marks:"))
if marks>80 and marks<=100:
    print("you scored an A")
elif marks>60 and marks<=80:
    print("you scored a B")
elif marks>50 and marks<=60:
    print("you scored a C")
elif marks>40 and marks<=50:
    print("you scored a D")
elif marks>30 and marks<=40:
    print("you have an E")
elif marks>=0 and marks<=30:
    print("you have failed")
else:
    print("Invalid input")
