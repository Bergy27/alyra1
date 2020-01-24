CASH_BASE = 100

def calculateChange(cash, ordre, _in, _out):
	return(cash*ordre[_out]/ordre[_in])


def calculateYield(path):
	cash = CASH_BASE
	path_length = len(path)
	for index, element in enumerate(path):
		if (index<path_length-1):
			currentOrder = list(filter(lambda ordre : element in ordre and path[index+1] in ordre, ordres))
			cash = calculateChange(cash, currentOrder[0], element, path[index+1])
	if cash>CASH_BASE:
		print("This path : "+str(path)+" is beneficial")
		print("If you had "+str(CASH_BASE)+" "+path[0]+", after one lap, you have "+str(cash)+" "+path[-1]+" now.\n")



def perm(monnaies):
	final = []
	if len(monnaies)==1:
		return [monnaies]
	else:
		for i in range(len(monnaies)):
			for j in perm(monnaies[:i]+monnaies[i+1:]):
				final.append(j + monnaies[i:i+1])
		return final

ordres = [
	{
		"doge" : 84,
		"ltc" : 32,
	},
	{
		"doge" : 29,
		"eth" : 80,
	},
	{
		"eth" : 300,
		"btc" : 62,
	},
	{
		"ltc" :288,
		"eth" : 2304
	},
	{
		"btc" : 27,
		"doge" : 46
	},
	{
		"btc" : 33,
		"ltc" : 16
	}
]

cryptos = ["doge", "ltc", "btc", "eth"]
permutations = perm(cryptos)
for i in range(len(cryptos)):
	for x in perm(cryptos[:i]+cryptos[i+1:]):
		permutations.append(x)

for permutation in permutations:
	permutation.append(permutation[0])
	calculateYield(permutation)
	#print(permutation)

