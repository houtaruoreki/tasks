from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def display_details(self):
        pass

    @abstractmethod
    def average_grade(self, grades):
        pass


class StudentMixin(Person):
    def average_grade(self, *args):
        n = 0
        if len(args) != 0:

            student = self.students[args[0]]
            for k in student.grades:
                n += student.grades[k]
            return n / len(student.grades)
        else:
            for k in self.grades:
                n += self.grades[k]
            return n / len(self.grades)

    def display_details(self, *args):
        if len(args) != 0:

            print(f"average grade for Student Management system {self.students[kwargs['student_id']].name}")
        else:
            print(f"average grade for student class {self.name}")
        pass


class Student(StudentMixin):
    def __init__(self, student_id, name, grades: dict):
        self._student_id = student_id
        self.name = name
        self.grades = grades

    def add_grade(self, subject, grade):
        try:
            if grade >= 0:
                self.grades[subject] = grade
            else:
                raise Exception("grade must be greater than 0")
        except Exception as msg:
            print(msg)

    @property
    def average_grade(self):
        return super().average_grade()


class StudentManagementSystem(StudentMixin):
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name: str, grades: dict):
        try:
            if student_id not in self.students:
                self.students[student_id] = Student(student_id, name, grades)
                print(f"student with id of {student_id} has been created")
            else:
                raise Exception(f"User with id {student_id} already exists")
        except Exception as msg:
            print(msg)


student_1 = Student(1, "luka", {"math": 60, "english": 80})
system = StudentManagementSystem()
# student_1.display_details()
system.add_student(1, "luka", {"math": 80})
# system.add_student(1, "luka", {"math": 80})
print(student_1.average_grade)
print(system.average_grade(1))
