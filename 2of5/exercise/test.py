class Car:
	def __init__(self, mark):
		self.mark = mark
		self.model = 'romeo'

	def __str__(self):
		return str(self.model)

c = Car("fiat")
print c