class Student:
    def __init__(self, name, grade, password):
        self.name = name              #PUBLIC
        self.grade = grade            #PROTECTED
        self.__password = password    #PRIVATE
    def display_info(self):
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Password:", self.__password)
    def change_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
        else:
            print("Password too short")
student1 = Student("ALice", "A", "secret123")
print(student1.name)
print(student1.grade)
student1.display_info()
student1.change_password("newpass123")
student1.display_info()