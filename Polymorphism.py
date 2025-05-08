#one can act as many
#two types of polymorphism
        #over loading
        #over riding

#over loading
     #Two or more methods have same name but different parameters

# def product(a, b):
#     p = a  * b
#     print(p)
#
# def product(a, b, c):
#     p = a *b * c
#     print(p)
# product(4, 5, 5)

#over riding
class Vehicle:
    def start(self):
        print("starting the vehicle")
class Car(Vehicle):
    def start(self):
        print("starting the car")
v = Vehicle()
c = Car()

v.start()
c.start()





