class Student(object):
    def __init__(self,name,id,marks):
        self.name = name
        self.id = id
        self.marks = marks

    def getName(self):
        return self.name
    def getId(self):
        return self.id
s = Student("Zaw ",13,123)
print(s.getName())
print(s.getId())

