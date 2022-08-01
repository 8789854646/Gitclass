class A:
	def demo(self):
		print("Print Parent class")

class B(A):
	def demo(self):
		print("Print Child Class")

class C(B):
	def demo(self):
		print("Print C Class")

c = C()



