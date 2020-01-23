from random import randint

#chr(65)=A
#chr(91)=Z

def rechercheDebut(chaine, n):
	essai=0
	if len(chaine)>n:
		return "impossible"
	while True:
		tirage = chaineAlea(n)
		essai+=1
		#print(tirage)
		if chaine==tirage[0:len(chaine)]:
			return essai




def chaineAlea(n):
	res = ""
	while n>0:
		res+=chr(randint(65,90))
		n-=1
	return res


#Testons pour 1, 2, 3 et 4 caractères (1000 fois chacun pour faire une moyenne)
for i in [1, 2, 3]:
	#init du nombre d'essais total pour 1000 tirages
	essaisTotal = 0
	for j in range(0, 1000):
		#On tire au sort la chaine de n caractères à trouver
		chaineATrouver = chaineAlea(i)
		essaisTotal += rechercheDebut(chaineATrouver, i)
	print("Pour {} caractères, il faut en moyenne {} tirages avant de trouver la bonne combinaison".format(i, essaisTotal/1000))



	#print(i)
#for i in range(0,1000):
#	chaineATrouver = 
#	rechercheDebut
#	print(i)
#print(rechercheDebut("AAAAAAAA", 8))