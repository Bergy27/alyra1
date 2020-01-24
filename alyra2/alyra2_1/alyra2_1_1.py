#https://learnmeabitcoin.com/guide/target
CIBLE_MAX = ((2**16-1)*2**208)

def cibleToDifficulte(cible):
	return CIBLE_MAX/cible

#initial target (Block 0)
target0 = "00000000ffff0000000000000000000000000000000000000000000000000000"

#current target (Block 614,308)
target614308 = "000000000000000000130c780000000000000000000000000000000000000000"

#should be 1
diff0 = cibleToDifficulte(int(target0, 16))
print(diff0)

#current difficulties
diff614308 = cibleToDifficulte(int(target614308, 16))
print(diff614308)

