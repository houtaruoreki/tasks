class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
class StudentMixin:
    def format_attributes(self):
        attributes = ', '.join([f"{attr}: {getattr(self, attr)}" for attr in vars(self)])
        return attributes
    
class Student(StudentMixin, Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university


