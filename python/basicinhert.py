class animal:
    def speak(self):
        print("animal make sound")
class Dog(animal): #writing animal means inheriting its class if we remove it , it gives attribute error
    def bark(self):
        print("dog bark")

dog = Dog()
dog.speak()#by writting animal we inherited its object
dog.bark()

4


