#python3 alyra1_4_5.py "12" "4" "-" "2" "*" --> 16 (ok)
#python3 alyra1_4_5.py "12" "4" "+" "2" "*" --> 32 (ok)
#python3 alyra1_4_5.py "12" --> 12 (ok)
#python3 alyra1_4_5.py "3" "4" "1" "2" "+" "*" "+" --> 15 (ok)
import sys


def calcPolonaiseInversee(pile, tas):
	#print("Pile  : "+str(pile))
	#print("Tas : "+str(tas))
	if len(tas)==0:
		return pile[0]
	if tas[0] in ["+", "*", "-", "/"]:
		arg2 = int(pile.pop())
		arg1 = int(pile.pop())
		if tas[0]=="+":
			return calcPolonaiseInversee(pile+[arg1+arg2], tas[1:])
		elif tas[0]=="-":
			return calcPolonaiseInversee(pile+[arg1-arg2], tas[1:])
		elif tas[0]=="*":
			return calcPolonaiseInversee(pile+[arg1*arg2], tas[1:])
		elif tas[0]=="/":
			return calcPolonaiseInversee(pile+[arg1/arg2], tas[1:])
	else:
		 return calcPolonaiseInversee(pile+[tas[0]], tas[1:])

a = calcPolonaiseInversee([], sys.argv[1:])
print(a)