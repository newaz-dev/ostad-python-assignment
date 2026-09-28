from typing import override


class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email       # Encapsulation
        self.age = age
        self.department = department

    # Getter for private email
    def get_email(self):
        return self.__email

    def display_info(self):
        print("\nStudent Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

    # Method Overloading using default argument
    def calculate_result(self, marks=None):
        if marks is None:
            print("Result: Marks not provided")
            return

        if marks >= 80:
            grade = "A+"
        elif marks >= 75:
            grade = "A"
        elif marks >= 70:
            grade = "A-"
        elif marks >= 65:
            grade = "B+"
        elif marks >= 60:
            grade = "B"
        elif marks >= 55:
            grade = "B-"
        elif marks >= 50:
            grade = "C+"
        elif marks >= 45:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"

        print(f"Marks: {marks}")
        print(f"Grade: {grade}")

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        semester
    ):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    @override
    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")

    @override
    def get_student_type(self):
        return "Undergraduate Student"


class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        research_topic
    ):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    @override
    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")

    @override
    def get_student_type(self):
        return "Graduate Student"


# ==========================================================
# Creating Objects
# ==========================================================

student1 = Student(
    "Md Shah Newaz Fahmir Hridoy",
    "0242310005101739",
    "newaz.fahmir@gmail.com",
    24,
    "Computer Science & Engineering"
)

student2 = UndergraduateStudent(
    "Rahim Ahmed",
    "0242310005101740",
    "rahim@gmail.com",
    25,
    "Computer Science & Engineering",
    "6th"
)

student3 = GraduateStudent(
    "Karim Hasan",
    "0242310005101741",
    "karim@gmail.com",
    26,
    "Computer Science & Engineering",
    "Deep Learning for Medical Image Analysis"
)


# ==========================================================
# Display Student Information
# ==========================================================

student1.display_info()
print(f"Student Type: {student1.get_student_type()}")
student1.calculate_result(78)


student2.display_info()
print(f"Student Type: {student2.get_student_type()}")
student2.calculate_result(88)


student3.display_info()
print(f"Student Type: {student3.get_student_type()}")
student3.calculate_result(72)


# ==========================================================
# Method Overloading Demonstration
# ==========================================================

print("\nMethod Overloading Demonstration:")

student1.calculate_result()
student1.calculate_result(85)


# ==========================================================
# Polymorphism Demonstration
# ==========================================================

print("\nPolymorphism Demonstration:")

students = [student1, student2, student3]

for student in students:
    print(f"{student.name} -> {student.get_student_type()}")