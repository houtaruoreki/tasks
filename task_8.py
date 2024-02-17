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
        if len(args) != 0:
            grades = self.students[args[0]].grades
        else:
            grades = self.grades
        n = 0
        for k in grades:
            n += grades[k]

        return n / len(grades)

    def display_details(self, *args):
        if len(args) != 0:
            student = self.students[args[0]]
            return f"ID - {student.student_id}, Name - {student.name}, Average Grade - {student.average_grade}"
        else:
            return f"ID - {self.student_id}, Name - {self.name}, Average Grade - {self.average_grade}"


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

    @property
    def display_details(self):
        return super().display_details()

    @property
    def student_id(self):
        return self._student_id


class StudentManagementSystem(StudentMixin):
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name: str, grades: dict):
        try:
            if student_id not in self.students:
                self.students[student_id] = Student(student_id, name, grades)
            else:
                raise Exception(f"User with id {student_id} already exists")
        except Exception as msg:
            print(msg)



