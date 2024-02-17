from abc import ABC, abstractmethod


class Person(ABC):
    @staticmethod
    @abstractmethod
    def display_student_info(student):
        pass

    @staticmethod
    @abstractmethod
    def average_grade(grades):
        pass


class StudentInfo(Person):
    @staticmethod
    def average_grade(grades: dict):
        if not grades:
            return 0
        n = 0
        for key in grades:
            n += grades[key]

        return int(n / len(grades))

    @staticmethod
    def display_student_info(student):
        return f"Id - {student.student_id}, name - {student.name}, average grade - {student.average_grade}"


class Student:
    def __init__(self, student_id: int, name: str, grades: dict):
        self._student_id = student_id
        self.name = name
        self.grades = grades
        self.average = 0

    def add_grade(self, grade, subject):
        self.grades[subject] = grade

    @property
    def average_grade(self):
        self.average = StudentInfo().average_grade(self.grades)
        return self.average

    def display_student_info(self):
        return StudentInfo().display_student_info(self)

    @property
    def student_id(self):
        return self._student_id


class StudentManagementSystem:
    def __init__(self, students=None):
        if not students:
            self.students = {}
        self.students = students
        self.student_info = ""

    def add_student(self, student_id, student: Student):
        self.students[student_id] = student

    def show_student_details(self, student_id):
        self.student_info = StudentInfo().display_student_info(self.students[student_id])
        return self.student_info


g = {
    "math": 81,
    "history": 70,
    "english": 51
}

student_1 = Student(1, "luka", g)
student_2 = Student(2, "jemal", g)
student_3 = Student(3, "giorgi", g)

students_ = {1: student_1, 2: student_2, 3: student_3}

obj = StudentManagementSystem(students_)

