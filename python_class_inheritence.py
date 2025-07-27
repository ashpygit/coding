class Car:
    def __init__(self,number_of_wheels,color,capacity):
        self.number_of_wheels=number_of_wheels
        self.color=color
        self.capacity=capacity
    
    def speed(self):
        return "Speed of the car is superb"

my_electric_car=Car(4,'blue',7)
print(my_electric_car.number_of_wheels) #4

class ElectricCar(Car):
    def __init__(self,number_of_wheels,color,capacity):
        Car.__init__(self,number_of_wheels,color,capacity)
        Car.speed(self)


e1=ElectricCar(4,'Red',2)
print(e1.color)
print(e1.speed())