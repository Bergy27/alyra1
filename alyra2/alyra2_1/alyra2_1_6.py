import math

CHANGEMENT = 210000
INITIAL_REWARD_BTC = 50
INITIAL_REWARD_SATOSHI = 100000000*INITIAL_REWARD_BTC

def recompenseBlocEnSatoshi(hauteurBloc):
	return math.floor(INITIAL_REWARD_SATOSHI/2**(math.floor(hauteurBloc/CHANGEMENT)))

def bitcoinsEnCirculation(hauteurBloc):
	reward_satoshi = 100000000*INITIAL_REWARD_BTC

	total = 0

	#Nombre de de fois que 210'000 rentre entièrement dans la hauteur du bloc
	loop = hauteurBloc//CHANGEMENT


	#On calcule le total de BTC tous les 210'000 blocs
	for i in range(loop):
		total += reward_satoshi*CHANGEMENT
		reward_satoshi = math.floor(reward_satoshi/2)


	#On calcule le reste des BTC (de la hauteur de bloc divisible par 210'000 jusqu'au bloc actuel)
	reste = hauteurBloc%CHANGEMENT+1
	total += reste*recompenseBlocEnSatoshi(hauteurBloc)

	#Conversion en BTC
	return total/100000000

print(bitcoinsEnCirculation(0))

print(bitcoinsEnCirculation(210000))

print(bitcoinsEnCirculation(2100001))