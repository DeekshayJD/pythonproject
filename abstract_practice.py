from abc import ABC, abstractmethod

# Abstract class representing a vehicle
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method for starting the vehicle
    @abstractmethod
    def start(self):
        print("car got started")

# Concrete subclass Car inheriting from Vehicle
class Car(Vehicle):
    def start(self):
        print(f"{self.name} starts with a key")

# Concrete subclass Bike inheriting from Vehicle
class Bike(Vehicle):
    def start(self):
        print(f"{self.name} starts with a kick")

# Create instances of Car and Bike
car = Car("Toyota")
bike = Bike("Honda")

# Call start method on instances
car.start()  # Output: Toyota starts with a key
bike.start()  # Output: Honda starts with a kick
