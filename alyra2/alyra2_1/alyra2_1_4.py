#Cible = coefficient * 2 ** (8*(exposant-3))
#Cible = CiblePrécédente x (bloc[Actuel].date - block[Actuel-2016].date) /(deux semaines en secondes)
#estimation difficulté : https://btc.com/stats/diff
#https://btc.com/block?date=2018-12-18
#timestamp to date http://www.timestamp.fr/?

TWO_WEEKS_IN_SECONDS=1209600

def calculerCible(dateBlock, dateBlockPrec, ciblePrec):
	return ciblePrec*(dateBlock-dateBlockPrec)/TWO_WEEKS_IN_SECONDS


#height 550368
#date 2018-11-17 00:51:24
#diff 6,653,303,141,405
dateBlock1 = 1542415884
BITS1 = "0x172a4e2f"
exposant1 = BITS1[2:4]
coefficient1 = BITS1[4:10]
cible1 = int(coefficient1, 16) * 2 ** (8*(int(exposant1, 16)-3))

#height 552384
#date 2018-12-03 12:59:28
#diff 5,646,403,851,534
dateBlock2 = 1543841968
BITS2 = "0x1731d97c"
exposant2 = BITS2[2:4]
coefficient2 = BITS2[4:10]
cible2 = int(coefficient2, 16) * 2 ** (8*(int(exposant2, 16)-3))

nouvelleCible = calculerCible(dateBlock2, dateBlock1, cible1)
print(nouvelleCible)