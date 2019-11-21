from functools import reduce

def calcul_pourboire(taille_max, choix):
	pourboire = 0
	taille = 0
	choix = list(map(lambda c:bool(int(c)), choix))
	for index, transaction in enumerate(transactions):
		if choix[index]:
			pourboire+=transaction["pourboire"]
			taille+=transaction["taille"]
	if taille<=taille_max:
		return (pourboire, choix)
	else:
		return (0, choix)

transactions = [
	{
		"taille" : 2000,
		"pourboire" : 13000
	},
	{
		"taille" : 6000,
		"pourboire" : 9000
	},
	{
		"taille" : 800,
		"pourboire" : 2000
	},
	{
		"taille" : 700,
		"pourboire" : 1500
	},
	{
		"taille" : 1200,
		"pourboire" : 3500
	},
	{
		"taille" : 1000,
		"pourboire" : 2800
	},
	{
		"taille" : 1300,
		"pourboire" : 5000
	},
	{
		"taille" : 600,
		"pourboire" : 1500
	},
]
bloc = 6000
pourboire_max=0

for i in range (0,2**len(transactions)):
	pourboire_actuel = calcul_pourboire(bloc, "{0:08b}".format(i))
	if pourboire_max<pourboire_actuel[0]:
		pourboire_max=pourboire_actuel[0]
		combinaison_ideale=pourboire_actuel[1]
print(pourboire_max)
print(combinaison_ideale)

	


