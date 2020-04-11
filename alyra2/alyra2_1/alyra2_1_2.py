#Le champ Bits de l’en-tête s’agit d’un nombre sur 256 bits enregistré sous la forme d’un cœfficient et d’un exposant.
#Cible = coefficient * 2 ** (8*(exposant-3))
#Le premier octet du champ Bits détermine l’exposant et les trois suivant le cœfficient.

CIBLE_MAX = ((2**16-1)*2**208)

def cibleToDifficulte(cible):
	print(cible)
	return CIBLE_MAX/cible

def calculerDifficulte(bits):
	exp = bits[2:4]
	coeff = bits[4:10]
	return cibleToDifficulte(int(coeff,16)*2**(8*(int(exp,16)-3)))


#print(calculerDifficulte("0x1c0ae493"))
#print(calculerDifficulte("0x03000001"))
print(calculerDifficulte("0x1800d0f6"))
