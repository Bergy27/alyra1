import datetime
import math

DATE_BLOC_1 = datetime.datetime(2009, 1, 9, 3, 54)
CHANGEMENT = 210000
INITIAL_REWARD_BTC = 50
INITIAL_REWARD_SATOSHI = 100000000*INITIAL_REWARD_BTC

def getStatusFromDate(date):
	minutes = minutesBetweenTwoDates(DATE_BLOC_1, date)
	hauteur_bloc = hauteurBloc(minutes)
	return {
		"actual_reward" : recompenseBlocEnSatoshi(hauteur_bloc)/100000000,
		"btc_outstanding" : bitcoinsEnCirculation(hauteur_bloc)
	}  


def minutesBetweenTwoDates(date_initial, date_final):
	return (date_final - date_initial)//datetime.timedelta(minutes=1)

def hauteurBloc(minutesSinceBloc1):
	return 1+minutesSinceBloc1//10

#alyra2_1_6
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

date_today = datetime.datetime.now()


print(getStatusFromDate(date_today))
