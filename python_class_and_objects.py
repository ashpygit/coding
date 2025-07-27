class Vehicle:
    pass

####################################################################################

my_car = Vehicle()
print(my_car); #<__main__.Vehicle object at 0x0000020BAE2F5700>

class Vehicle:
    def __init__(self, number_tyres, color, seating_capacity):
        self.number_tyres = number_tyres
        self.color = color
        self.seating_capacity = seating_capacity

tesla_model_x1 = Vehicle(4,'Red',6)
print(tesla_model_x1.number_tyres) # 4
tesla_model_x1.number_tyres=3
print(tesla_model_x1.number_tyres) # 3
print(tesla_model_x1.color) # Red

#####################################################################################

class Vehicle:
    def __init__(self, number_tyres, color, seating_capacity):
        self.number_tyres = number_tyres
        self.color = color
        self.seating_capacity = seating_capacity

    def number_tyres_med(self):
        print("Self Made Car with number of tyres: 4")
    
tesla_model_x2 = Vehicle(6,'Blue',7)

tesla_model_x2.number_tyres_med()

#####################################################################################

class Student:

    school = 'Telusko'

    def __init__(self,name,rollno,percent):
        self.name = name
        self.rollno = rollno
        self.percent = percent

    def grade(self):
        if self.percent < 40:
            print(self.name,"has failed")
        elif self.percent >=40 and self.percent <= 50:
            print(self.name,"secured grade C")
        elif self.percent >= 50 and self.percent <= 60:
            print(self.name,"secured grade B")
        else:
            print("Congratulations!!",self.name,"secured grade A")

    @classmethod
    def showgrade(cls):
        print('This Student class belongs to',cls.school,'School')
                   
s1 = Student('Akash',2,67)
s2 = Student('Bashi',4,40)
s3 = Student('Kashi',7,30)

s1.school='Vydehi'
print("object calling class variable",s1.school)
print("object calling class variable",s2.school)

Student.school='Sarafa'

s2.school='Vydehi'

print("object calling class variable",s1.school)
print("object calling class variable",s2.school)
print("object calling class variable",s3.school)

Student.showgrade()




