class Student:
    college = ''

    def __init__(self, name, age=None, marks=None):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        return '##### {} - College #####\nName: {}\nAge: {}\nMarks: {}\n'.format(self.college, self.name, self.age, self.marks)


college = Student.college = 'VBIR'
s1 = Student('Ramu', 20, 900)
print(s1.display())
