class Student:
    def __init__(self,name,reg_no,course):
        self.myname=name
        self.myreg_no=reg_no
        self.mycourse=course
    def Database(self):

class Gender(Student):
    def __init__(self,name,reg_no,course,stud_age):
        super().__init__(name,reg_no,course)
        self.mystud_age=stud_age
    def Students(self):
        print(f"{self.myname},{self.myreg_no},{self.mystud_age}")
gender=Gender("Ambrose","7659/2020",30)
gender.Database()
