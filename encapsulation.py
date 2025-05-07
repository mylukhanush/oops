class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
person1 = Person("Alice", 30)
print(person1.name)
print(person1.get_age())
person1.set_age(35)
print(person1.get_age())
person1.set_age(-5)