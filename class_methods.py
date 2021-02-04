# Instance method to process data of the objects


class Student:
    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m

    def display(self):
        return 'Student Name is {} and he is secured marks {}'.format(self.name, self.marks)

    def cal(self):
        if self.marks >= 700:
            return 'You have passed the exam in first class'
        elif self.marks >= 500:
            return 'You have passed the exam in second class'
        elif self.marks >= 300:
            return 'You have passed the exam in third class'
        else:
            return 'You have failed the exam, please try again'


n = int(input('How many students?: '))

i = 0
while i < n:
    name = str(input('Enter student name: '))
    marks = int(input('Enter student marks: '))
    s = Student(name, marks)
    print(s.display())
    print(s.cal())
    i += 1

#############################################
# Accessor and Mutator instance methods in class


class Student:

    # Mutator instance method
    def set_name(self, n):
        self.name = n

    # Accessor instance method
    def get_name(self):
        return 'Student name is {}'.format(self.name)

    # Mutator instance method
    def set_college(self, col):
        self.col = col

    # Accessor instance method
    def get_college(self):
        return 'Student studying in college {}'.format(self.col)


s = Student()
s.set_name('Bharath')
s.set_college('ibm')
print(s.get_name())
print(s.get_college())

####################################
# Class method


class Vehicle:
    tyre = 4

    @classmethod
    def display(cls, car):
        cls.car = car
        return "{} has {} tyres".format(cls.car, cls.tyre)


car = Vehicle.display('maruti')
print(car)

####################################
# Static method


class MyClass:
    n = 0

    def __init__(self):
        MyClass.n += 1

    @staticmethod
    def static_method():
        return 'No. of instances created: {}'.format(MyClass.n)


c1 = MyClass()
c2 = MyClass()
c3 = MyClass()
print(c1.static_method())

####################################
