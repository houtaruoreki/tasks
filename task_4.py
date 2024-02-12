class Student:
    university = None
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade:
{self.grade}"
    @property
    def is_passing(self):
        if self.grade>60:
            return True
        else: return False
    
    def increse_grade(self,value):
        self.grade +=value