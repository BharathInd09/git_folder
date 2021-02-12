# Static Method

class CountObj:
    c = 0

    def __init__(self):
        CountObj.c = CountObj.c + 1

    @staticmethod
    def objcount():
        return "count of obects {}".format(CountObj.c)


c1 = CountObj()
c2 = CountObj()
c2 = CountObj()
print(c1.objcount())