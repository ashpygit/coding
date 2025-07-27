class A:

    def __init__(self):
         print("Calling init  from A")
         self.execute()                

    def execute(self):
        print("Calling exe from A")

class B(A):

    def __init__(self):
         print("Calling init from B")     

    def execute(self):
        print("Calling exe from B")

class C:
    
    def callme(self,ide):
        ide.execute()

ide = A()
ide = B()
ide.execute()