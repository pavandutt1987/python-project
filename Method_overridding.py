class Animal:
    def sound(self):
        print("Animal Sounds")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
dog = Dog()
dog.sound()