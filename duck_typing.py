class Duck:
	def talk(self):
		return 'quack, quack!'


class Human:
	def talk(self):
		return 'hello, hi!'


def call_obj(obj):
    print(obj.talk())

p1 = Duck()
call_obj(p1)
