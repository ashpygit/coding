class Topten:

    def __init__(self):
        self.num=1

    def __iter__(self):
       print('iter is called')
  
       return self

    def __next__(self):
        print(f'next is called {self.num}')
        val = self.num
        self.num += 1    
        return val

a = Topten()
print(a.__next__())
print(a.__next__())
print("Loop Starts now")
for i in a:
    print(i)
    if i==10:
        break
    
