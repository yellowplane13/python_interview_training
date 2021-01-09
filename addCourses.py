class Student:
    def __init__(self, name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name, max_stds):
        self.name = name
        self.max_stds = max_stds
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_stds:
            self.students.append(student)
            return True
        return False
    
    def get_grade_avg(self):
        sum = 0

        for i in self.students:
            sum += i.get_grade()
            avg = sum / len(self.students)
        return avg
        

s1 = Student("tim", 13, 89)
s2 = Student("Bill", 14, 45)
s3 = Student("Jill", 14, 76)

course = Course("Eng", 2)
course.add_student(s1)
course.add_student(s2)

