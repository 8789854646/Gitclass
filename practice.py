class Parent:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def add(self):
		print("Print Parent class")
		return self.a + self.b
	def sub(self):
		self.add()

class Child(Parent):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def mul(self):
		print("Print Child Class")
		return self.a * self.b

p = Parent(25, 36)

vivek




