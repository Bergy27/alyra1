#0 --> 50 bitcoins
#209'999 -> 50 bitcoins
#210'000 -> 25 bitcoins
#Cette récompense, qui est incluse dans la transaction coinbase avec les frais collectés, est en effet divisée par deux (arrondi à l’entier inférieur en Satoshis) tous les 210 000 blocs
#Elle était initialement de 50 bitcoins et de 12,5 bitcoins aujourd’hui.
#Trouver récompense : https://www.blockchain.com/btc/block/000000000000048b95347e83192f69cf0366076336c639f9b7228e9ba171342e
#100,000,000 sathoshi = 1 btc
import math

CHANGEMENT = 210000
INITIAL_REWARD_BTC = 50
INITIAL_REWARD_SATOSHI = 100000000*INITIAL_REWARD_BTC

def recompenseBloc(hauteurBloc):
	return math.floor(INITIAL_REWARD_SATOSHI/2**(math.floor(hauteurBloc/CHANGEMENT)))/100000000

	#print("coucou")


print(recompenseBloc(0))
print(recompenseBloc(209999))
print(recompenseBloc(210000))
print(recompenseBloc(420000))
print(recompenseBloc(614335))
#0.04882812
print(recompenseBloc(2100001))

