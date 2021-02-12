# Passing of one class to another class


class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print("ID: {}\nName: {}\nSal: {}".format(self.id, self.name, self.sal))


class AnotherClass:

    @staticmethod
    def mymethod(x):
        x.sal = x.sal + 1000
        x.display()


e = Emp('1023', 'Bharath', 1000)
AnotherClass().mymethod(e)
