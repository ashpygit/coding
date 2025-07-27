from threading import *
from time import sleep

class A(Thread): #class A is subclass of Thread
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

a = A()
b = B()

a.start()
sleep(0.2)
b.start()

a.join()  
b.join()
#join() is required to tell main thread to execute only after execution of thread a and thread b complete

print("bye") #this is considered main thread