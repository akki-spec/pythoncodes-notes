from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #no implementation
class Car(Vehicle):
    def start(self):
        print("car start with a key")
class Bike(Vehicle):
    def start(self):
        print("bike start with a button")

car = Car()
bike = Bike()

car.start()
bike.start()


