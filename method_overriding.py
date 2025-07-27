class A:
    def show(self):
        print("Calling A show")

class B(A):
    def show(self):
        print("Calling B show")

a = B()
a.show()