#champ bit 0x173218a5
#représente 0000000000000000003218a50000000000000000000000000000000000000000
#cible : 256 bits = 32 octets = 16


def cibleAtteinte(coefficient, exposant, hash):
	coefficient10 = int(coefficient,16)
	exposant10 = int(exposant, 16)
	cible = coefficient10 * 2 ** (8*(exposant10-3))
	if int(hash,16)<cible:
		return True
	else:
		return False

print(cibleAtteinte("3218a5","17", "0000000000000000003218a50000000000000000000000000000000000000001"))
print(cibleAtteinte("3218a5","17", "0000000000000000000218a50000000000000000000000000000000000000001"))


