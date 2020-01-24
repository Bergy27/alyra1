import math
class Cercle:
	def __init__(self, rayon):
		self.rayon = rayon

	def aire(self):
		return self.rayon**2*math.pi

	def perimetre(self):
		return 2*self.rayon*math.pi

c = Cercle(5)
print({'aire': c.aire(), 'perimetre': c.perimetre()})