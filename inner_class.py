class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = Student.Laptop()

    class Laptop:
        def __init__(self):
            self.comp = 'HP'
            self.ram = '16gb'
        
        def show_info(self):
            print(self.comp, self.ram)


    def show_info(self):
        print(self.name,self.age)
        self.lap.show_info()


s1 = Student('Arun',22)
s2 = Student('Saha',39)

s1.show_info()
print("")

s2.show_info()
