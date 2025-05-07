#Inheritance allows a class (child class) to acquire properties...
# ...and methods of another class (parent class)
#types of Inheritance:
        #single inheritance:A child class inherits from
# a single parent class.
        #Multiple Inheritance: A child class inherits from
# more than one parent class.
        #Multilevel Inheritance: A child class inherits from
# a parent class, which in turn inherits from another class.


# Single Inheritance
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def display_name(self):
#         print(f"Dog's Name: {self.name}")
#
# class Labrador(Dog):  # Single Inheritance
#     def sound(self):
#         print("Labrador woofs")

# Multilevel Inheritance
# class GuideDog(Labrador):  # Multilevel Inheritance
#     def guide(self):
#         print(f"{self.name}Guides the way!")
#
# Multiple Inheritance
# class Friendly:
#     def greet(self):
#         print("Friendly!")
#
# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# Example Usage
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()
#
# guide_dog = GuideDog("Max")
# guide_dog.display_name()
# guide_dog.guide()
#
# retriever = GoldenRetriever("Charlie")
# retriever.display_name()
# retriever.greet()
# retriever.sound()

#single inheritance
class vehicle :
    def show(self):
        print("This is Vehicle")
class car(vehicle):
    def drive(self):
        print("Car is Driving") 
# c = car()
# c.show()
# c.drive()
#Multilevel inheritance
class ElectricCar(car):
    def charge(self):
        print("electric car need to charge")
# ec = ElectricCar()
# ec.show()
# ec.drive()
# ec.charge()



