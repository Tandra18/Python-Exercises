class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self,grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0

student = Student(name='Alice',age=50,grades=[23,45,23])
student.add_grade(78)
print(student.get_average_grade())