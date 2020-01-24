#0 --> 50 bitcoins
#209'999 -> 50 bitcoins
#210'000 -> 25 bitcoins
#Elle était initialement de 50 bitcoins et de 12,5 bitcoins aujourd’hui.
#Trouver récompense : https://www.blockchain.com/btc/block/000000000000048b95347e83192f69cf0366076336c639f9b7228e9ba171342e
import math

CHANGEMENT = 210000
INITIAL_REWARD = 50

def recompenseBloc(hauteurBloc):
	return INITIAL_REWARD/2**(math.floor(hauteurBloc/CHANGEMENT))

	#print("coucou")


print(recompenseBloc(0))
print(recompenseBloc(209999))
print(recompenseBloc(210000))
print(recompenseBloc(420000))
print(recompenseBloc(614335))