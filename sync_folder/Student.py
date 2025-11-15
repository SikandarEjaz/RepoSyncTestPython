class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_student_id(self):
        return self.student_id
    
    def set_student_id(self, student_id):
        self.student_id = student_id
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade
    
    def print_info(self):
        print(f"Student: {self.name}, ID: {self.student_id}, Grade: {self.grade}")
    
    def is_passing(self):
        if self.grade >= 60:
            return True
        return False
    