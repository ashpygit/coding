class Student:
    def marks(self,a=None,b=None,c=None):
        s = a+b+c
        return s


s1 = Student()
s1_marks=s1.marks()
print(s1_marks)