#y²=x³+ax +b
class CourbeElliptique:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		if 4*a**3+27*b**2 == 0:
			raise ValueError('({}, {}) n\'est pas une courbe valide'.format(a, b))

	def __eq__(self, x):
		if self.a==x.a and self.b==x.b:
			return True
		return False

	def testPoint(self, x, y):
		if x**3+self.a*x+self.b==y**2:
			print("Le point ({},{}) appartient à la courbe.".format(x,y))
		else:
			print("Le point ({},{}) n'appartient pas à la courbe.".format(x,y))

	def __str__(self):
		return "a = "+str(self.a)+"; b ="+str(self.b)





c1 = CourbeElliptique(3,4)
c2 = CourbeElliptique(3,4)
c3 = CourbeElliptique(-4,1)
print(c1==c2)
print(c1==c3)
c1.testPoint(1,2)
c3.testPoint(-1, 2)
print(str(c1))
print(str(c3))