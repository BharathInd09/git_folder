class Student:
    college = ''

    def __init__(self, name, age=None, marks=None, add):
        self.name = name
        self.age = age
        self.marks = marks
        self.add = 'Florida'

    def display(self):
        return '##### {} - College #####\nName: {}\nAge: {}\nMarks: {}\nAddress: {}\n'.format(self.college, self.name, self.age, self.marks, self.add)


college = Student.college = 'VBIR'
s1 = Student('Ramu', 20, 900,)
print(s1.display())
