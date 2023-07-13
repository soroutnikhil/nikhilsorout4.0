# Ans1 
class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_speed):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed= max_speed
        self.average_speed=average_speed
car = vehicle("car" ,200,100)
print(car.name_of_vehicle)    
print(car.max_speed)          
print(car.average_speed)      


# Ans 2
class vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
        
        

class car(vehicle):
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} people."
            
car = car("Tesla Model S", 200, 30)
capacity =6
print(car.seating_capacity(capacity)) 


# Ans 3
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def fly(self):
        print(f"{self.name} is flying.")


class Bird(Animal):
    def __init__(self, name):
       super().__init__(name)


bird = Bird("Sparrow")
bird.eat()  
bird.sleep()  
bird.fly()  

# Ans 4
# In Python, getters and setters are methods used to access and modify the attributes of a class. 
class MyClass:
    def __init__(self):
        self._my_attribute = None

    def get_my_attribute(self):
        return self._my_attribute

    def set_my_attribute(self, value):
        self._my_attribute = value
my_object = MyClass()
print(my_object.get_my_attribute()) 
my_object.set_my_attribute(42)
print(my_object.get_my_attribute()) 


# Ans 5
# Method overriding in Python is a feature that allows a subclass to provide a different implementation of a method that is already defined in its superclass
class Shape:
    def area(self):
        print("Calculating area in the Shape class.")

class Rectangle(Shape):
    def area(self):
        print("Calculating area in the Rectangle class.")


my_shape = Shape()
my_rectangle = Rectangle()


my_shape.area()  
my_rectangle.area() 
