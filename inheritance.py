class A:
    def f1(self):
        print("Class A f1 calling...")

    def f2(self):
        print("Class A f2 calling...")

class B(A):
    def f3(self):
        print("Class B f3 calling...")

    def f4(self):
        print("Class B f4 calling...")

class C(B):
    def f5(self):
        print("Class C f5 calling...")
    
a1 = A()
c1 = C()

a1.f1()
a1.f2()

c1.f1()  #C1 calling feature of class A
c1.f2() #C1 calling feature of class A
c1.f3() #C1 calling feature of class B
c1.f4() #C1 calling feature of class B
c1.f5() 