from typing import override

class Student:
    def __init__(self, name, student_id, email, age, department):
      self.name = name
      self.student_id = student_id
      self.email = email
      self.age = age
      self.department = department

    def display_info(self):
      print("\n")
      print("Student Information:")
      print(f"Name: {self.name}")
      print(f"ID: {self.student_id}")
      print(f"Email: {self.email}")
      print(f"Age: {self.age}")
      print(f"Department: {self.department}")
      print("\n")


    def calculate_result(self):
     pass

    def get_student_type(self):
      pass 


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
     self.semester = semester

     super().__init__(name, student_id, email, age, department)


    @override
    def get_student_type(self):
        pass



class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
      self.research_topic = research_topic
      super().__init__(name, student_id, email, age, department)

    @override
    def get_student_type(self):
       pass

student1 = Student("Md Shah Newaz Fahmir Hridoy", "0242310005101739", "newaz.fahmir@gmail.com", "24", "Computer Science & Engineering")
student1.display_info()