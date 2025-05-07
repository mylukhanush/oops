# object oriented programming
# oops principles
        #classes
        #objects
        #Inheritance
        #Encapsulation
        #Polymorphism
        #Abstraction

#Classes
# class is a collection of object
# classes are blueprint for creating a object

# class Dog:
#     species = "rock"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#Explanation:
#class Dog:Defines a class named Dog
#Species:A class attribute shared by all instances of the class
#__init__method:initializes the name and age attributes....
#...when a new object is created


#Object
#It represents a specific implementation of the class and
# holds its own data.
#State: It is represented by the attributes and reflects the....
# ...properties of an object.
# Behavior: It is represented by the methods of an object and...
# ...reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables...
# ....one object to interact with other objects.

# class Dog:
#     species = "Canine"  # Class attribute
#
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# Creating an object of the Dog class
# class Dog:
#     species = "Canine"  # Class attribute
#
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute
#
# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)
#
# print(dog1.name)
# print(dog1.species)

#Explanation:
#dog1 = Dog("Buddy", 3):Creates an object of the dog class...
#...with name as "Buddy" and age as 3
#dog1.name: Accesses the instance attribute species of the...
#...dog1 object.
#dog1.species:Accesses the class attribute spicies of the...
#...dog1 object

class House:
    material = "bricks"
    def __init__(self, length, price):
        self.length = length
        self.price = price

# client1 = House(5,20000)
# client2 = House(7,40000)
# print(client1.material)
# print(client1.length)
# print(client1.price)

# class House2:
#     material = "cement"
#    def __init__(self,length, price):
#         self.length = length
#         self.price = price
# client1 = House2(10,50000)
# client2 = House2(15, 80000)
#
#     class House3:
#         material = "iron"
#         def __init__(self,length, price):
#              self.length = length
#              self.price = price
#     client1 = House3(20, 90000)
#     client2 = House3(25, 95000)



